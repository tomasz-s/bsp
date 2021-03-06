"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

def instantiateComponent(bspComponent):

    internalDDRPartsList = ["PIC32MZ2064DAH169",
                            "PIC32MZ2064DAG169",
                            "PIC32MZ2064DAR169",
                            "PIC32MZ2064DAS169"]

    externalDDRPartsList = ["PIC32MZ2064DAA288",
                            "PIC32MZ2064DAB288"]

    if (Variables.get("__PROCESSOR") in internalDDRPartsList):
        # LED 1: RH0
        Database.setSymbolValue("core", "BSP_PIN_151_FUNCTION_TYPE", "LED_AH")
        Database.setSymbolValue("core", "BSP_PIN_151_FUNCTION_NAME", "LED1")
        Database.setSymbolValue("core", "BSP_PIN_151_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_151_DIR", "Out")
        Database.setSymbolValue("core", "BSP_PIN_151_LAT", "")

        # LED 2: RH2
        Database.setSymbolValue("core", "BSP_PIN_103_FUNCTION_TYPE", "LED_AH")
        Database.setSymbolValue("core", "BSP_PIN_103_FUNCTION_NAME", "LED2")
        Database.setSymbolValue("core", "BSP_PIN_103_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_103_DIR", "Out")
        Database.setSymbolValue("core", "BSP_PIN_103_LAT", "")

        # LED 3: RH1
        Database.setSymbolValue("core", "BSP_PIN_150_FUNCTION_TYPE", "LED_AH")
        Database.setSymbolValue("core", "BSP_PIN_150_FUNCTION_NAME", "LED3")
        Database.setSymbolValue("core", "BSP_PIN_150_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_150_DIR", "Out")
        Database.setSymbolValue("core", "BSP_PIN_150_LAT", "")

        #Switch 1: RB13
        Database.setSymbolValue("core", "BSP_PIN_72_FUNCTION_TYPE", "SWITCH_AL")
        Database.setSymbolValue("core", "BSP_PIN_72_FUNCTION_NAME", "SWITCH1")
        Database.setSymbolValue("core", "BSP_PIN_72_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_72_PU", "True")
        Database.setSymbolValue("core", "BSP_PIN_72_DIR", "")

        # Switch 2: RB12
        Database.setSymbolValue("core", "BSP_PIN_26_FUNCTION_TYPE", "SWITCH_AL")
        Database.setSymbolValue("core", "BSP_PIN_26_FUNCTION_NAME", "SWITCH2")
        Database.setSymbolValue("core", "BSP_PIN_26_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_26_PU", "True")
        Database.setSymbolValue("core", "BSP_PIN_26_DIR", "")

        # Switch 3: RB14
        Database.setSymbolValue("core", "BSP_PIN_62_FUNCTION_TYPE", "SWITCH_AL")
        Database.setSymbolValue("core", "BSP_PIN_62_FUNCTION_NAME", "SWITCH3")
        Database.setSymbolValue("core", "BSP_PIN_62_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_62_PU", "True")
        Database.setSymbolValue("core", "BSP_PIN_62_DIR", "")

    elif (Variables.get("__PROCESSOR") in externalDDRPartsList):
        # LED 1: RH0
        Database.setSymbolValue("core", "BSP_PIN_283_FUNCTION_TYPE", "LED_AH")
        Database.setSymbolValue("core", "BSP_PIN_283_FUNCTION_NAME", "LED1")
        Database.setSymbolValue("core", "BSP_PIN_283_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_283_DIR", "Out")
        Database.setSymbolValue("core", "BSP_PIN_283_LAT", "")

        # LED 2: RH1
        Database.setSymbolValue("core", "BSP_PIN_246_FUNCTION_TYPE", "LED_AH")
        Database.setSymbolValue("core", "BSP_PIN_246_FUNCTION_NAME", "LED2")
        Database.setSymbolValue("core", "BSP_PIN_246_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_246_DIR", "Out")
        Database.setSymbolValue("core", "BSP_PIN_246_LAT", "")

        # LED 3: RH2
        Database.setSymbolValue("core", "BSP_PIN_206_FUNCTION_TYPE", "LED_AH")
        Database.setSymbolValue("core", "BSP_PIN_206_FUNCTION_NAME", "LED3")
        Database.setSymbolValue("core", "BSP_PIN_206_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_206_DIR", "Out")
        Database.setSymbolValue("core", "BSP_PIN_206_LAT", "")

        #Switch 1: RB12
        Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_TYPE", "SWITCH_AL")
        Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_NAME", "SWITCH1")
        Database.setSymbolValue("core", "BSP_PIN_33_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_33_PU", "True")
        Database.setSymbolValue("core", "BSP_PIN_33_DIR", "")

        # Switch 2: RB13
        Database.setSymbolValue("core", "BSP_PIN_54_FUNCTION_TYPE", "SWITCH_AL")
        Database.setSymbolValue("core", "BSP_PIN_54_FUNCTION_NAME", "SWITCH2")
        Database.setSymbolValue("core", "BSP_PIN_54_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_54_PU", "True")
        Database.setSymbolValue("core", "BSP_PIN_54_DIR", "")

        # Switch 3: RB14
        Database.setSymbolValue("core", "BSP_PIN_143_FUNCTION_TYPE", "SWITCH_AL")
        Database.setSymbolValue("core", "BSP_PIN_143_FUNCTION_NAME", "SWITCH3")
        Database.setSymbolValue("core", "BSP_PIN_143_MODE", "DIGITAL")
        Database.setSymbolValue("core", "BSP_PIN_143_PU", "True")
        Database.setSymbolValue("core", "BSP_PIN_143_DIR", "")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx2")

    BSP_NAME = "pic32mz_da_sk"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
        {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
        {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
        {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
            {"type":"SWITCH_AH", "mode":"DIGITAL"},
            {"type":"SWITCH_AL", "mode":"DIGITAL"},
            {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT","lat":"High"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
