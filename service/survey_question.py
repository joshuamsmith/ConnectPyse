from ..cw_model import CWModel


class SurveyQuestion(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.sequenceNumber = None  # (Integer)
        self.type = None  # *(Enum)
        self.question = None  # *(String(1000))
        self.options = None  # (SurveyQuestionOption[])
        self.includeFlag = None  # (Boolean)
        self.requiredFlag = None  # (Boolean)
        self.noAnswerPoints = None  # (Integer)
        self.surveyId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
