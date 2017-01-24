from ..cw_model import CWModel


class KnowledgeBaseArticle(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.title = None  # *(String)
        self.issue = None  # *(String)
        self.resolution = None  # *(String)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self.boardId = None  # (Integer)
        self.categoryId = None  # (Integer)
        self.subCategoryId = None  # (Integer)
        self.dateCreated = None  # (String)
        self.createdBy = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
