from ..cw_model import CWModel


class ProjectTeamMember(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.projectId = None  # (Integer)
        self.hours = None  # (Number)
        self.member = None  # *(MemberReference)
        self.projectRole = None  # *(ProjectRoleReference)
        self.workRole = None  # (WorkRoleReference)
        self.startDate = None  # (String)
        self.endDate = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
