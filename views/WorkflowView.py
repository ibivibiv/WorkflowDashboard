# /src/views/WorkflowView.py
from flask import request, g, Blueprint, json, Response

from models.WorkflowModel import WorkflowModel, WorkflowSchema

workflow_api = Blueprint('workflow_api', __name__)
workflow_schema = WorkflowSchema()


@workflow_api.route('/', methods=['GET'])
def get_all():
    """
    Get All Workflows
    """
    posts = WorkflowModel.get_all_workflows()
    data = workflow_schema.dump(posts, many=True).data
    return custom_response(data, 200)


@workflow_api.route('/<int:workflow_id>', methods=['GET'])
def get_one(workflow_id):
    """
    Get A Workflow
    """
    record = WorkflowModel.get_one_workflow(workflow_id)
    if not record:
        return custom_response({'error': 'record not found'}, 404)
    data = workflow_schema.dump(record).data
    return custom_response(data, 200)


@workflow_api.route('/workflowId/<workflow_id>', methods=['GET'])
def get_by_workflow_id(workflow_id):
    """
    Get A Workflow
    """
    records = WorkflowModel.get_workflow_by_wfId(workflow_id)
    data = workflow_schema.dump(records, many=True).data
    return custom_response(data, 200)


@workflow_api.route('/html/workflowId/<workflow_id>', methods=['GET'])
def get_by_workflow_wfId(workflow_id):
    """
    Get A Workflow
    """
    records = WorkflowModel.get_workflow_by_wfId(workflow_id)

    response = '<table border=2 style="width:100%">'
    response +="<tr><th>workflow id</th><th>workflow name</th><th>status</th><th>create time</th><th>start time</th><th>update time</th><th>end time</th></tr>"

    for record in records:
        response += "<tr><th>" + record.workflowId + "</th><th>" + record.workflowName + "</th><th>" + record.status + "</th><th>" + str(
            record.createTime) + "</th><th>" + str(record.startTime) + "</th><th>" + str(
            record.updateTime) + "</th><th>" + str(record.endTime) + "</th></tr>"

    response += "</table>"
    return response


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
