Title: Intel Composer XE 2013 SP1 & VTune
Date: 2013-07-17
Tags: HPC, Intel, YAR
Slug: hpc003
Author: hpczone
Summary: Intel Composer XE 2013 SP1 & VTune

After long delay, I am finally able to write something here.. Last few days I
spent figuring out why VTune 2013 U12 & 13 freezes after profiling an app..

To make long story short, on some OpenMP applications Intel Compose XE 2013 SP1
(compiler version 14.0.0) doesn't play well with VTune XE 2013. The sympots of
this behaviour is manifested by VTune printing tons of

    ...
    Logging fork
    Logging fork
    ...

during profiling. After processing the data, VTune finds its enough and
freezes.  This freeze repeats after restarting VTune and atteming to open the
profiling data in the Project Navigator.

The cause of this is libiomp5.so in 

    /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/mic/libiomp5.so
    /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/ia32/libiomp5.so
    /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/intel64/libiomp5.so

This is the only library that is found while grepping "Logging fork" in Intel's
stuff. I know that VTune XE works fine with Intel Composer XE 2013 update 13
(compiler version 13.1.3), so I just copied libiomp5.so 

    cp /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/mic/libiomp5.so   /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/mic/
    cp /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/ia32/libiomp5.so   /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/ia32/
    cp /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/intel64/libiomp5.so   /opt/intel/composer_xe_2013_sp1.0.080/compiler/lib/mic/

This allows to use both Intel compiler 14.0.0 and profile the app in VTune.
Hopefully intel will fix bug soon ...
