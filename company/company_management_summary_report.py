from ..cw_model import CWModel


class CompanyManagementSummaryReport(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.managementSolution = None  # (ManagementSolutionReference)
        self.groupIdentifier = None  # *(String(100))
        self.deviceType = None  # (Enum)
        self.agreement = None  # (AgreementReference)
        self.snmpMachines = None  # (Integer)
        self.totalWorkstations = None  # (Integer)
        self.totalServers = None  # (Integer)
        self.totalWindowsServers = None  # (Integer)
        self.totalWindowsWorkstations = None  # (Integer)
        self.totalManagedMachines = None  # (Integer)
        self.serversOffline = None  # (Integer)
        self.serversDiskSpaceLow = None  # (Integer)
        self.failedBackupJobs = None  # (Integer)
        self.totalNotifications = None  # (Integer)
        self.successfulBackupJobs = None  # (Integer)
        self.serverAvailability = None  # (Integer)
        self.virusesRemoved = None  # (Integer)
        self.spywareItemsRemoved = None  # (Integer)
        self.windowsPatchesInstalled = None  # (Integer)
        self.diskCleanups = None  # (Integer)
        self.diskDefragmentations = None  # (Integer)
        self.fullyPatchedMachines = None  # (Integer)
        self.missingOneTwoPatchesMachines = None  # (Integer)
        self.missingThreeFivePatchesMachines = None  # (Integer)
        self.missingMoreFivePatchesMachines = None  # (Integer)
        self.missingUnscannedPatchesMachines = None  # (Integer)
        self.alertsGenerated = None  # (String)
        self.internetConnectivity = None  # (Number)
        self.diskSpaceCleanedMb = None  # (Integer)
        self.missingSecurityPatches = None  # (String)
        self.cpuUtilization = None  # (Number)
        self.memoryUtilization = None  # (Number)
        self.company = None  # (CompanyReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
