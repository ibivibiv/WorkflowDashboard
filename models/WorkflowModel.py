# src/models/Workflow.py
from . import db
from marshmallow import fields, Schema
import time


class WorkflowModel(db.Model):
    """
    Workflow Model
    """

    __tablename__ = 'workflow'

    id = db.Column(db.Integer, primary_key=True)
    correlationId = db.Column(db.String(128))
    createdBy = db.Column(db.String(128))
    createTime = db.Column(db.Integer)
    endTime = db.Column(db.Integer)
    index = db.Column(db.String(128))
    ownerApp = db.Column(db.String(128))
    parentWorkflowId = db.Column(db.String(128))
    reasonForIncompletion = db.Column(db.String(128))
    reRunFromWorkflowId = db.Column(db.String(128))
    schemaVersion = db.Column(db.Integer)
    startTime = db.Column(db.Integer)
    status = db.Column(db.String(128))
    updatedBy = db.Column(db.String(128))
    updateTime = db.Column(db.Integer)
    version = db.Column(db.Integer)
    workflowId = db.Column(db.String(128))
    workflowName = db.Column(db.String(128))
    workflowVersion = db.Column(db.Integer)

    def __init__(self, data):
        self.id = data.get('id')
        self.correlationId = data.get('correlationId')
        self.createdBy = data.get('createdBy')
        self.createTime = data.get('createTime')
        self.endTime = data.get('endTime')
        self.index = data.get('index')
        self.ownerApp = data.get('ownerApp')
        self.parentWorkflowId = data.get('parentWorkflowId')
        self.reasonForIncompletion = data.get('reasonForIncompletion')
        self.reRunFromWorkflowId = data.get('reRunFromWorkflowId')
        self.schemaVersion = data.get('schemaVersion')
        self.startTime = data.get('startTime')
        self.status = data.get('status')
        self.updatedBy = data.get('updatedBy')
        self.updateTime = data.get('updateTime')
        self.version = data.get('version')
        self.workflowId = data.get('workflowId')
        self.workflowName = data.get('workflowName')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updateTime = int(round(time.time() * 1000))
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_workflows():
        return WorkflowModel.query.all()

    @staticmethod
    def get_one_workflow(id):
        return WorkflowModel.query.get(id)

    @staticmethod
    def get_workflow_by_wfId(id):
        return WorkflowModel.query.filter_by(workflowId=id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class WorkflowSchema(Schema):
    """
    Workflow Schema
    """
    id = fields.Int(dump_only=True)
    correlationId = fields.Str()
    createdBy = fields.Str()
    createTime = fields.Int()
    endTime = fields.Int()
    index = fields.Str()
    ownerApp = fields.Str()
    parentWorkflowId = fields.Str()
    reasonForIncompletion = fields.Str()
    reRunFromWorkflowId = fields.Str()
    schemaVersion = fields.Int()
    startTime = fields.Int()
    status = fields.Str()
    updatedBy = fields.Str()
    updateTime = fields.Int()
    version = fields.Int()
    workflowId = fields.Str()
    workflowName = fields.Str()
    workflowVersion = fields.Int()
