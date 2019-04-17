# Visit 2.10.2 log file
ScriptVersion = "2.10.2"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
ShowAllWindows()
Source("/Users/miller86/Applications/VisIt.app/Contents/Resources/2.10.2/darwin-x86_64/bin/makemovie.py")
ToggleCameraViewMode()
SetTimeSliderState(0)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0000"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(1)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0001"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(2)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0002"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(3)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0003"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(4)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0004"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(5)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0005"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(6)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0006"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(7)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0007"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(8)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0008"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(9)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0009"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(10)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0010"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(11)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0011"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(12)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0012"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(13)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0013"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(14)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0014"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(15)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0015"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(16)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0016"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(17)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0017"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(18)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0018"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(19)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0019"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(20)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0020"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(21)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0021"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(22)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0022"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(23)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0023"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(24)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0024"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(25)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0025"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(26)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0026"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(27)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0027"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(28)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0028"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(29)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0029"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(30)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0030"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(31)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0031"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(32)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0032"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(33)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0033"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(34)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0034"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(35)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0035"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(36)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0036"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(37)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0037"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(38)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0038"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(39)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0039"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(40)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0040"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(41)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0041"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(42)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0042"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(43)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0043"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(44)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0044"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(45)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0045"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(46)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0046"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(47)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0047"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(48)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0048"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(49)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0049"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(50)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0050"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(51)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0051"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(52)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0052"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(53)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0053"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(54)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0054"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(55)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0055"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(56)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0056"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(57)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0057"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(58)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0058"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(59)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0059"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(60)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0060"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(61)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0061"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(62)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0062"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(63)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0063"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(64)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0064"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(65)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0065"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(66)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0066"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(67)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0067"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(68)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0068"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(69)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0069"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(70)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0070"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(71)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0071"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(72)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0072"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(73)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0073"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(74)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0074"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(75)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0075"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(76)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0076"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(77)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0077"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(78)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0078"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(79)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0079"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(80)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0080"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(81)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0081"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(82)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0082"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(83)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0083"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(84)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0084"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(85)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0085"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(86)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0086"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(87)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0087"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(88)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0088"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(89)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0089"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(90)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0090"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(91)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0091"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(92)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0092"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(93)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0093"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(94)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0094"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(95)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0095"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(96)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0096"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(97)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0097"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(98)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0098"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(99)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0099"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetTimeSliderState(100)
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/Users/miller86/fastmath/atpesc17_examples/ATPESC2018HandsOnLessons/foo"
SaveWindowAtts.fileName = "movie0100"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1590
SaveWindowAtts.height = 496
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.displayListMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 0
RenderingAtts.specularCoeff = 0.6
RenderingAtts.specularPower = 10
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
SetRenderingAttributes(RenderingAtts)
SetTimeSliderState(0)
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/miller86/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
