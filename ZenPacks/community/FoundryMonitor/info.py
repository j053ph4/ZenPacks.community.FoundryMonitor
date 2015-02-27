from ZenPacks.community.ConstructionKit.ClassHelper import *

def snChasFangetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class snChasFanInfo(ClassHelper.snChasFanInfo):
    ''''''

def snAgentCpugetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class snAgentCpuInfo(ClassHelper.snAgentCpuInfo):
    ''''''

def snChasPwrSupplygetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class snChasPwrSupplyInfo(ClassHelper.snChasPwrSupplyInfo):
    ''''''

def snAgentTempgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class snAgentTempInfo(ClassHelper.snAgentTempInfo):
    ''''''


