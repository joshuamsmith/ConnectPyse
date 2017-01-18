from ..cw_model import CWModel


class Configuration(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # (String(100))*
        self.type = None  # (ConfigurationTypeReference)*
        self.status = None  # (ConfigurationStatusReference)
        self.company = None  # (CompanyReference)*
        self.contact = None  # (ContactReference)
        self.site = None  # (SiteReference)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self.deviceIdentifier = None  # (String(100))
        self.serialNumber = None  # (String(250))
        self.modelNumber = None  # (String(50))
        self.tagNumber = None  # (String(50))
        self.purchaseDate = None  # (String)
        self.installationDate = None  # (String)
        self.installedBy = None  # (MemberReference)
        self.warrantyExpirationDate = None  # (String)
        self.vendorNotes = None  # (String)
        self.notes = None  # (String)
        self.macAddress = None  # (String(25))
        self.lastLoginName = None  # (String(100))
        self.billFlag = None  # (Boolean)
        self.backupSuccesses = None  # (Integer)
        self.backupIncomplete = None  # (Integer)
        self.backupFailed = None  # (Integer)
        self.backupRestores = None  # (Integer)
        self.lastBackupDate = None  # (String)
        self.backupServerName = None  # (String(50))
        self.backupBillableSpaceGb = None  # (Number)
        self.backupProtectedDeviceList = None  # (String)
        self.backupYear = None  # (Integer)
        self.backupMonth = None  # (Integer)
        self.ipAddress = None  # (String(50))
        self.defaultGateway = None  # (String(50))
        self.osType = None  # (String(250))
        self.osInfo = None  # (String(250))
        self.cpuSpeed = None  # (String(100))
        self.ram = None  # (String(25))
        self.localHardDrives = None  # (String)
        self.parentConfigurationId = None  # (Integer)
        self.vendor = None  # (CompanyReference)
        self.manufacturer = None  # (ManufacturerReference)
        self.questions = None  # (Array)
        self.activeFlag = None  # (Boolean)
        self.managementLink = None  # (String(200))
        self.remoteLink = None  # (String(200))
        self.sla = None  # (SLAReference)
        self.mobileGuid = None  # (Guid)
        self._info  = None  # (Metadata)
        self.customFields = None  # (Array)

        # initialize object with json dict
        super().__init__(json_dict)
