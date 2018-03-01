################################################################################
#### Component ####
################################################################################

def instantiateComponent(sst26Component):
    sst26PLIB = sst26Component.createStringSymbol("SST26_PLIB", None)
    sst26PLIB.setLabel("PLIB Used")
    sst26PLIB.setReadOnly(True)

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    sst26HeaderFile = sst26Component.createFileSymbol(None, None)
    sst26HeaderFile.setSourcePath("sst26/sst26.h")
    sst26HeaderFile.setOutputName("sst26.h")
    sst26HeaderFile.setDestPath("external_peripheral/sst26/")
    sst26HeaderFile.setProjectPath("config/" + configName + "/external_peripheral/sst26/")
    sst26HeaderFile.setType("HEADER")
    sst26HeaderFile.setOverwrite(True)

    sst26SourceFile = sst26Component.createFileSymbol(None, None)
    sst26SourceFile.setSourcePath("sst26/templates/sst26.c.ftl")
    sst26SourceFile.setOutputName("sst26.c")
    sst26SourceFile.setDestPath("external_peripheral/sst26/")
    sst26SourceFile.setProjectPath("config/" + configName + "/external_peripheral/sst26/")
    sst26SourceFile.setType("SOURCE")
    sst26SourceFile.setOverwrite(True)
    sst26SourceFile.setMarkup(True)

    sst26SystemDefFile = sst26Component.createFileSymbol(None, None)
    sst26SystemDefFile.setType("STRING")
    sst26SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sst26SystemDefFile.setSourcePath("sst26/templates/system/system_definitions.h.ftl")
    sst26SystemDefFile.setMarkup(True)

    sst26SystemInitFile = sst26Component.createFileSymbol(None, None)
    sst26SystemInitFile.setType("STRING")
    sst26SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS")
    sst26SystemInitFile.setSourcePath("sst26/templates/system/system_initialize.c.ftl")
    sst26SystemInitFile.setMarkup(True)

def onDependentComponentAdded(sst26Component, id, remoteComponent):
    if id == "sst26_QSPI_dependency" :
        plibUsed = sst26Component.getSymbolByID("SST26_PLIB")
        plibUsed.clearValue()
        plibUsed.setValue(remoteComponent.getID().upper(), 2)
