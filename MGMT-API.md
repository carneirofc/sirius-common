## /getAllPVs
Get all the PVs in the cluster. Note this call can return millions of PVs

**:param pv:** An optional argument that can contain a GLOB wildcard. We will return PVs that match this GLOB. For example, if pv=KLYS*, the server will return all PVs that start with the string KLYS. If both pv and regex are unspecified, we match against all PVs.

**:param regex:**  An optional argument that can contain a Java regex wildcard. We will return PVs that match this regex. For example, if pv=KLYS*, the server will return all PVs that start with the string KLYS.

**:param limit:**  An optional argument that specifies the number of matched PV's that are retured. If unspecified, we return 500 PV names. To get all the PV names, (potentially in the millions), set limit to –1.

## /getPVStatus
Get the status of a PV.

**:param pv:** The name(s) of the pv for which status is to be determined. If a pv is not being archived, you should get back a simple JSON object with a status string of "Not being archived." You can also pass in GLOB wildcards here and multiple PVs as a comma separated list. If you have more PVs that can fit in a GET, send the pv's as a CSV pv=pv1,pv2,pv3 as the body of a POST.

## /getPVTypeInfo
Get the type info for a given PV. In the archiver appliance terminology, the PVTypeInfo contains the various archiving parameters for a PV.

**:param pv:** The name of the pv.

## /archivePV
Archive one or more PV's.

**:param pv:** The name of the pv to be archived. If archiving more than one PV, use a comma separated list. You can also send the PV list as part of the POST body using standard techniques. If you need to specify different archiving parameters for each PV, send the data as a JSON array (remember to send the content type correctly).

**:param samplingperiod:** The sampling period to be used. Optional, default value is 1.0 seconds.

**:param samplingmethod:** The sampling method to be used. For now, this is one of SCAN or MONITOR. Optional, default value is MONITOR.

**:param controllingPV:** The controlling PV for coditional archiving. Optional; if unspecified, we do not use conditional archiving.

**:param policy:** Override the policy execution process and use this policy instead. Optional; if unspecified, we go thru the normal policy execution process.

**:param appliance:** Optional; you can specify an appliance in a cluster. If specified (value is the identity of the appliance), the sampling and archiving are done on the specified appliance.


## /pauseArchivingPV
Pause archiving the specified PV. This also tears down the CA channel for this PV.

**:param pv:** The name of the pv. You can also pass in GLOB wildcards here and multiple PVs as a comma separated list. If you have more PVs that can fit in a GET, send the pv's as a CSV pv=pv1,pv2,pv3 as the body of a POST.


## /resumeArchivingPV
Resume archiving the specified PV.

**:param pv:** The name of the pv. You can also pass in GLOB wildcards here and multiple PVs as a comma separated list. If you have more PVs that can fit in a GET, send the pv's as a CSV pv=pv1,pv2,pv3 as the body of a POST.


## /getStoresForPV
Gets the names of the data stores for this PV. Every store in a PV's typeinfo is expected to have a name - this is typically "name=STS" or something similar. This call returns the names of all the stores for a PV.

**:param pv:** The name of the pv.


## /consolidateDataForPV
Consolidate the data for this PV until the specified store. The PV needs to be paused first.

**:param pv:** The name of the pv.

**:param storage:** The name of the store until which we'll consolidate data. This is typically a string like STS or MTS. To get a list of names of stores for a PV, please see /getStoresForPV/deletePV - Stop archiving the specified PV. The PV needs to be paused first.


**:param pv:** The name of the pv.

**:param deleteData:** Should we delete the data that has already been recorded. Optional, by default, we do not delete the data for this PV. Can be true or false.


## /abortArchivingPV
Abort any pending requests for archiving this PV.

**:param pv:** The name of the PV.


## /changeArchivalParameters
Change the archival parameters for a PV.

**:param pv:** The name of the pv.

**:param samplingperiod:** The new sampling period in seconds.

**:param samplingmethod:** The new sampling method For now, this is one of SCAN or MONITOR.


## /getPVDetails
Get a lot of detailed statistics for a PV. The returned JSON is very UI friendly; but should be usable in a scripting environment.

**:param pv:** The name of the pv.


## /getApplianceInfo
Get the appliance information for the specified appliance.

**:param id:** The identity of the appliance for which we are requesting information. This is the same string as the identity element in the appliances.xml that identifies this appliance.


## /getAppliancesInCluster
Get the appliance information for all the appliances in the cluster that are active.

## /renamePV
Rename this pv to a new name. The PV needs to be paused first.

**:param pv:** The current name of the PV.

**:param newname:** The new name of the PV.


## /reshardPV pv

The name of the pv. The PV needs to be paused first and will remain in a paused state after the resharding is complete.
**:param appliance:** The new appliance to assign the PV to. This is the same string as the identity element in the appliances.xml that identifies this appliance.

**:param storage:** The name of the store until which we'll consolidate data before resharding. The data is moved over to the store with the same name on the new appliance. This is typically a string like LTS.


## /appendAndAliasPV
This BPL appends the data for an older PV into a newer PV. The older PV is deleted and an alias mapping the older PV name to the new PV is added.

**:param olderpv:** The name of the older pv. The data for this PV will be appended to the newer PV and then deleted.

**:param newerpv:** The name of the newer pv.

**:param storage:** The name of the store until which we'll consolidate data before appending. This is typically a string like LTS.


## /addAlias
Add an alias for the specified PV.

**:param pv:** The real name of the pv.

**:param aliasname:** The alias name of the pv. Note, we cannot have a PVTypeInfo mapped to the alias name.


## /removeAlias
Remove an alias for the specified PV. This is only supported for PVs who have completed their archive PV workflow.

**:param pv:** The real name of the pv.

**:param aliasname:** The alias name of the pv.


## /skipAliasCheck
For PVs that are still in the archive PV workflow, skip the alias check where we examine the .NAME field to determine the real name. This is useful if you have pCAS servers that overload the .NAME field for something else.

**:param pv:** The name of the pv as it is in the archive PV workflow.


## /changeTypeForPV
Change the type of the PV to the specified type. The PV needs to be paused first. For best results, consolidate all the data to one store. Note, this is actually changing the data so you should make a backup just in case. There is every chance that this may leave the data for this PV in an inconsistent state. It is also possible that the plugin may do nothing in which case you may have to rename the existing PV to a new PV; delete this PV and issue a fresh archival request.

**:param pv:** The name of the pv.

**:param newtype:** The new type one of the ArchDBRTypes. For example, DBR_SCALAR_DOUBLE.


## /getVersions
Get the versions of the various components for this appliance.

**:param id:** The identity of the appliance for which we are requesting information. This is the same string as the identity element in the appliances.xml that identifies this appliance.


## /modifyMetaFields
Modify the fields (HIHI, LOLO etc) being archived as part of the PV. PV needs to be paused first.

**:param pv:** The real name of the pv.

**:param command:** A command is a verb followed by a list of fields, all of them comma separated. Possible verbs are add, remove and clear. For example add,ADEL,MDEL will add the fields ADEL and MDEL if they are not already present. clear clears all the fields. You can have any number of commands.


## /getNamedFlag
Get the value of the named flag specified by name

**:param name:** the name of the named flag.


## /setNamedFlag
Set the value of the named flag specified by name

**:param name:** the name of the named flag.

**:param value:** Either true of false; something that Boolean.parse can understand.


## /getNeverConnectedPVs
Get a list of PVs that have never connected.

## /getMetaGets
Get a list of PVs that are currently in METAINFO_REQUESTED state.

## /getCurrentlyDisconnectedPVs
Get a list of PVs that are currently disconnected.

## /getEventRateReport
Return a list of PVs sorted by descending event rate.

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getStorageRateReport
Return a list of PVs sorted by descending storage rate.

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getRecentlyAddedPVs
Return a list of PVs sorted by descending PVTypeInfo creation timestamp.

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getRecentlyModifiedPVs
Return a list of PVs sorted by descending PVTypeInfo modification timestamp.

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getLostConnectionsReport
Return a list of PVs sorted by number of times we've lost/reestablished connections (descending) to the IOC hosting the PV. Can be used to determine if the IOC is being overloaded.

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getSilentPVsReport
Return a list of PVs sorted by the timestamp of the last event received (descending).

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getPVsByDroppedEventsTimestamp
Return a list of PVs sorted by number of times we've lost events because of incorrect timestamps.

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getPVsByDroppedEventsBuffer
Return a list of PVs sorted by number of times we've lost events because of buffer overflows; perhaps from a mismatch between the event rate and the sampling rate (as determined from the sampling period).

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getPausedPVsReport
Return a list of PVs that are currently paused.

**:param limit:** Limit this report to this many PVs per appliance in the cluster. Optional, if unspecified, there are no limits enforced.


## /getArchivedWaveforms
Get a list of waveform PVs that are currently being archived.

## /getTimeSpanReport
Archiving time span; when we first added the PV to the system, last known timestamp (if available), paused or not.

## /getMatchingPVsForThisAppliance
Get matching PV's for this appliance. Specify one of pv or regex. If both are specified, we only apply the pv wildcard. If neither is specified, we return an empty list.

**:param pv:** An optional argument that can contain a GLOB wildcard. We will return PVs that match this GLOB. For example, if pv=KLYS*, the server will return all PVs that start with the string KLYS.

**:param regex:** An optional argument that can contain a Java regex wildcard. We will return PVs that match this regex. For example, if pv=KLYS.*, the server will return all PVs that start with the string KLYS.

**:param limit:** An optional argument that specifies the number of matched PV's that are returned. If unspecified, we return 500 PV names. To get all the PV names, (potentially in the millions), set limit to 1.


## /putPVTypeInfo
Updates the typeinfo for the specified PV. Note this merely updates the typeInfo. It does not have any logic to react to changes in the typeinfo. That is, don't assume that the PV is automatically paused just because you changed the isPaused to true. This is meant to be used in conjuction with other BPL to implement site-specific BPL in external code (for example, python). This can also be used to add PVTypeInfo's into the system; support for this is experimental. The new PVTypeInfo's are automatically paused before adding into the system. Logically, you have to specify at least one of override or createnew.

**:param pv:** The name of the pv.

**:param override:** If the PVTypeInfo for this PV already exists, do you want to update it or return an error? By default, this is false.

**:param createnew:** If the PVTypeInfo for this PV does not exist, do you want to create a new one or return an error? By default, this is false.


## /unarchivedPVs
Given a list of PVs, determine those that are not being archived/have pending requests/have aliases.

**:param pv:** A list of pv names. Send as a CSV using a POST or JSON array.


## /archivedPVs
Given a list of PVs, determine those that are being archived.

**:param pv:** A list of pv names. Send as a CSV using a POST.


## /archivedPVsNotInList
Given a list of PVs, determine those that are being archived but are not in the incoming list.

**:param pv:** A list of pv names. Send as a CSV using a POST, or as a JSON.

