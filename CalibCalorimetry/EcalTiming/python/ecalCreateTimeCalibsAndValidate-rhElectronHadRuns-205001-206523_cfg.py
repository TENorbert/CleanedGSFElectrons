import FWCore.ParameterSet.Config as cms

process = cms.Process("EcalCreateTimeCalibrations")

# Global Tag -- for original timing calibrations
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.GlobalTag.globaltag = 'GR_P_V40::All'
process.GlobalTag.globaltag = 'GR_P_V42::All'
#process.GlobalTag.globaltag = 'GR_P_V41::All'

#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")                                                                          
 # process.load("Configuration.StandardSequences.Geometry_cff")                
 # process.GlobalTag.globaltag = 'GR_P_V40::All'        

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(threshold = cms.untracked.string('INFO')),
    categories = cms.untracked.vstring('*'),
    destinations = cms.untracked.vstring('cout')
)

process.TFileService = cms.Service("TFileService", 
    fileName = cms.string("EcalCreateTimeCalibsAndValidate-rhElectronHadRuns-205001-206523.root"),
    closeFileFast = cms.untracked.bool(True)
    )


process.createTimeCalibs = cms.EDAnalyzer("EcalCreateTimeCalibrations",
  OutputFileName = cms.string("file:converted1.root"),##Not Used
  OutputTimeCalibFileName = cms.string("EcalTimeCalibConstants-Runs205001-206523.xml"),##Name of output xml file with new constants
  OutputTimeOffsetFileName = cms.string("EcalTimeOffset-Runs205001-206523.xml"),##Name of output xml file with new constants
  FileNameStart = cms.string("ecalCreateTimeCalibs"),
  ZeroGlobalOffset = cms.bool(False), ## if true, disables global offset
  SubtractDBcalibs = cms.bool(True),
  BxIncludeExclude = cms.string("-1"),
  OrbitIncludeExclude = cms.string("-1"),
  TriggerBitIncludeExclude = cms.string("-1"),
  TechTriggerBitIncludeExclude = cms.string("-1"),
  LumiIncludeExclude = cms.string("-1"),
  RunIncludeExclude = cms.string("205001-206523"),
  AvgTimeMin = cms.double(-5),
  AvgTimeMax = cms.double(5),
  MinHitAmpEB = cms.double(100),  
  MinHitAmpEE = cms.double(100), 
  MaxSwissCross = cms.double(0.95),
  MaxHitTimeEB = cms.double(5),
  MinHitTimeEB = cms.double(-5),
  MaxHitTimeEE = cms.double(7),
  MinHitTimeEE = cms.double(-7),
  EventsUsedFractionNum = cms.double(1),
  EventsUsedFractionDen = cms.double(1),
  InputFileNames = cms.vstring('file:/uscmst1b_scratch/lpc1/3DayLifetime/tnorbert/EcalTimeCalibs/rh-EleHad2012D-Prompreco-v1-RunR-203773-206510-Hadded-Nov12.root'

#'file:/uscms_data/d3/tnorbert/DataSets/EcalTimingTrees/EleHad2012C-Promptrecov2/rhElectronHadDataSet2012C-Promptreco-v2-Runrange-202233-203777-Col-Wed-Oct25-Ntuple.root'
#'file:/data/jared/data/EcalTiming/ElectronHadRuns-201187-201699/rh-ElectronHad_ElectronHad_Run2012C-PromptReco-v2_AOD-201187-201699.HADDED.root',
#      'file:/data/jared/data/EcalTiming/ElectronHadRuns-201670-202232/rh-ElectronHad_ElectronHad_Run2012C-PromptReco-v2_AOD-201670-202232.HADDED.root'
       )
)

process.expressValidator = cms.EDAnalyzer("EcalTimeCalibrationValidator",
  InputFileNames = cms.vstring('file:/uscmst1b_scratch/lpc1/3DayLifetime/tnorbert/EcalTimeCalibs/rh-EleHad2012D-Prompreco-v1-RunR-203773-206510-Hadded-Nov12.root'
#'file:/uscms_data/d3/tnorbert/DataSets/EcalTimingTrees/EleHad2012C-Promptrecov2/rhElectronHadDataSet2012C-Promptreco-v2-Runrange-202233-203777-Col-Wed-Oct25-Ntuple.root'
#'file:/data/jared/data/EcalTiming/ElectronHadRuns-201670-202232/rh-ElectronHad_ElectronHad_Run2012C-PromptReco-v2_AOD-201670-202232.HADDED.root',
#      'file:/data/jared/data/EcalTiming/ElectronHadRuns-201187-201699/rh-ElectronHad_ElectronHad_Run2012C-PromptReco-v2_AOD-201187-201699.HADDED.root'
),
OutputFileName = cms.string('file:/uscms_data/d3/tnorbert/DataSets/RecalibratedTrees/converted-rh-ElectronHad_ElectronHad_Run2012D-PromptReco-v1_AOD-205001-206523-Nov12.root'),
  CalibConstantXMLFileName = cms.string("EcalTimeCalibConstants-Runs205001-206523.xml"),
  CalibOffsetXMLFileName = cms.string("EcalTimeOffset-Runs205001-206523.xml"),
  ZeroGlobalOffset = cms.bool(False),## if true, does not use global shift
  MaxTreeEntriesToProcess = cms.untracked.int32(-1),
  RunIncludeExclude = cms.string("205001-206523")
)

process.recalibratedTimeHists = cms.EDAnalyzer("EcalCreateTimeCalibrations",
  OutputFileName = cms.string("file:converted1.root"),##Not Used
  OutputTimeCalibFileName = cms.string("Junk.xml"),## Important - Don't overwrite previous xml file!
  OutputTimeOffsetFileName = cms.string("JunkOffset.xml"),## Important - Don't overwrite previous xml file!
  FileNameStart = cms.string("ecalCreateTimeCalibsRecalibrated"),
  ZeroGlobalOffset = cms.bool(False),
  SubtractDBcalibs = cms.bool(True),
  BxIncludeExclude = cms.string("-1"),
  OrbitIncludeExclude = cms.string("-1"),
  TriggerBitIncludeExclude = cms.string("-1"),
  TechTriggerBitIncludeExclude = cms.string("-1"),
  LumiIncludeExclude = cms.string("-1"),
  RunIncludeExclude = cms.string("205001-206523"),
  AvgTimeMin = cms.double(-5),
  AvgTimeMax = cms.double(5),
  MinHitAmpEB = cms.double(100),  
  MinHitAmpEE = cms.double(100), 
  MaxSwissCross = cms.double(0.95),
  MaxHitTimeEB = cms.double(5),
  MinHitTimeEB = cms.double(-5),
  MaxHitTimeEE = cms.double(7),
  MinHitTimeEE = cms.double(-7),
  EventsUsedFractionNum = cms.double(1),
  EventsUsedFractionDen = cms.double(1),
  InputFileNames = cms.vstring('file:/uscms_data/d3/tnorbert/DataSets/RecalibratedTrees/converted-rh-ElectronHad_ElectronHad_Run2012D-PromptReco-v1_AOD-205001-206523-Nov12.root')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )
process.source = cms.Source("EmptySource",
       numberEventsInRun = cms.untracked.uint32(1),
       firstRun = cms.untracked.uint32(204000)
)
process.p = cms.Path(process.createTimeCalibs*process.expressValidator)
process.pEnd = cms.Path(process.recalibratedTimeHists)
process.schedule = cms.Schedule(process.p)
process.schedule.append(process.pEnd)
