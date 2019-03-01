from cw_model import CWModel


class Opportunity(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(100))
        self.expectedCloseDate = None  # (String)
        self.type = None  # (OpportunityTypeReference)
        self.stage = None  # (OpportunityStageReference)
        self.status = None  # (OpportunityStatusReference)
        self.priority = None  # (OpportunityPriorityReference)
        self.notes = None  # (String)
        self.probability = None  # (OpportunityProbabilityReference)
        self.source = None  # (String(50))
        self.rating = None  # (OpportunityRatingReference)
        self.campaign = None  # (CampaignReference)
        self.primarySalesRep = None  # *(MemberReference)
        self.secondarySalesRep = None  # (MemberReference)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self.company = None  # *(CompanyReference)
        self.contact = None  # *(ContactReference)
        self.site = None  # *(SiteReference)
        self.customerPO = None  # (String(25))
        self.pipelineChangeDate = None  # (String)
        self.dateBecameLead = None  # (String)
        self.closedDate = None  # (String)
        self.closedBy = None  # (MemberReference)
        self.totalSalesTax = None  # (Number)
        self.shipToCompany = None  # (CompanyReference)
        self.shipToContact = None  # (ContactReference)
        self.shipToSite = None  # (SiteReference)
        self.billToCompany = None  # (CompanyReference)
        self.billToContact = None  # (ContactReference)
        self.billToSite = None  # (SiteReference)
        self.billingTerms = None  # (BillingTermsReference)
        self.taxCode = None  # (TaxCodeReference)
        self._info = None  # (Metadata)
        self.customFields = None  # (CustomFieldValue[])

        # initialize object with json dict
        super().__init__(json_dict)
