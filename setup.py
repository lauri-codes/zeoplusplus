import sys
from setuptools import setup, find_packages
from setuptools.extension import Extension

# Check python version
if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

# The recommendation
# (https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules)
# is to distribute Cython compiled source files with the package. This is why
# the Cython compilation step is disabled by default here.
USE_CYTHON = True
ext = '.pyx' if USE_CYTHON else '.cpp'
language = "c++"
includedirs = ["src/voro++/src"]
cpp_extra_compile_args = ["-fPIC"]
netstorage_srcfiles = [
    'src/zeoplusplus/netstorage'+ext, 'src/networkstorage.cc', 
    'src/mindist.cc', 'src/geometry.cc', 'src/networkinfo.cc',
    'src/networkio.cc', 'src/grid.cc', 'src/symbcalc.cc',
    'src/string_additions.cc', 
    'src/voronoicell.cc', 
    'src/networkanalysis.cc', 'src/graphstorage.cc', 'src/area_and_volume.cc',
    'src/network.cc', 'src/OMS.cc', 'src/v_network.cc', 'src/symmetry.cc',
    'src/networkaccessibility.cc', 'src/channel.cc', 'src/net.cc', 'src/ray.cc',
	'src/rmsd.cc','src/material.cc', 'src/psd.cc',
]
netinfo_srcfiles = ['src/zeoplusplus/netinfo'+ext, 'src/networkinfo.cc']
netio_srcfiles = [
    'src/zeoplusplus/netio'+ext, 'src/networkio.cc', 
    'src/networkinfo.cc',  'src/string_additions.cc', 
    'src/grid.cc', 'src/mindist.cc', 'src/symbcalc.cc',  'src/symmetry.cc',
    'src/networkstorage.cc', 'src/geometry.cc', 'src/net.cc', 'src/rmsd.cc',
]
graphstorage_srcfiles = ['src/zeoplusplus/graphstorage'+ext, 'src/graphstorage.cc']
psd_srcfiles = ['src/zeoplusplus/psd'+ext, 'src/psd.cc']
voronoicell_srcfiles = [
    'src/zeoplusplus/voronoicell'+ext, 'src/voronoicell.cc', 'src/geometry.cc',
	'src/networkstorage.cc', 'src/net.cc', 'src/mindist.cc', 
	'src/networkinfo.cc', 'src/rmsd.cc', 'src/symmetry.cc', 
	'src/string_additions.cc', 'src/ray.cc', 'src/channel.cc', 
	'src/network.cc', 'src/OMS.cc', 'src/area_and_volume.cc', 'src/networkaccessibility.cc', 
	'src/graphstorage.cc', 'src/networkanalysis.cc', 'src/v_network.cc',
]
channel_srcfiles = ['src/zeoplusplus/channel'+ext, 'src/channel.cc']
highaccuracy_srcfiles = [
    'src/zeoplusplus/high_accuracy'+ext, 'src/sphere_approx.cc', 'src/networkstorage.cc', 
    'src/networkinfo.cc', 'src/mindist.cc', 'src/geometry.cc', 'src/net.cc', 
	'src/symmetry.cc', 'src/string_additions.cc', 'src/ray.cc',
	'src/networkaccessibility.cc', 'src/network.cc', 'src/networkio.cc',
	'src/grid.cc', 'src/symbcalc.cc', 'src/voronoicell.cc', 'src/graphstorage.cc',
	'src/channel.cc', 'src/v_network.cc', 'src/networkanalysis.cc',
	'src/area_and_volume.cc', 'src/rmsd.cc', 'src/material.cc', 'src/psd.cc',
]
areavol_srcfiles = [
    'src/zeoplusplus/area_volume'+ext, 'src/area_and_volume.cc', 'src/networkinfo.cc', 
    'src/networkstorage.cc', 'src/mindist.cc', 'src/geometry.cc', 
    'src/networkio.cc', 'src/grid.cc', 'src/symbcalc.cc',
    'src/string_additions.cc', 'src/voronoicell.cc',
    'src/networkanalysis.cc', 'src/graphstorage.cc', 'src/symmetry.cc', 
    'src/network.cc', 'src/OMS.cc', 'src/v_network.cc', 'src/ray.cc', 'src/rmsd.cc',
    'src/networkaccessibility.cc', 'src/channel.cc', 'src/net.cc'
]
cluster_srcfiles = [
    'src/zeoplusplus/cluster'+ext, 'src/cluster.cc', 'src/networkstorage.cc',
    'src/networkinfo.cc', 'src/mindist.cc', 'src/geometry.cc', 
    'src/network.cc', 'src/OMS.cc', 'src/voronoicell.cc', 'src/graphstorage.cc',
    'src/networkanalysis.cc', 'src/channel.cc', 'src/v_network.cc',
    'src/area_and_volume.cc',  'src/networkaccessibility.cc', 
    'src/string_additions.cc', 'src/sphere_approx.cc', 'src/net.cc',
	'src/symmetry.cc', 'src/ray.cc', 'src/rmsd.cc', 'src/material.cc', 'src/psd.cc',
]
cycle_srcfiles = [
    'src/zeoplusplus/cycle'+ext, 'src/cycle.cc', 'src/networkstorage.cc',
    'src/networkinfo.cc', 'src/mindist.cc', 'src/geometry.cc', 
    'src/network.cc', 'src/OMS.cc', 'src/voronoicell.cc', 'src/graphstorage.cc',
    'src/networkanalysis.cc', 'src/channel.cc', 'src/v_network.cc',
    'src/area_and_volume.cc',  'src/networkaccessibility.cc', 
    'src/string_additions.cc', 'src/sphere_approx.cc'
]
geometry_srcfiles = [
    'src/zeoplusplus/geometry'+ext, 'src/geometry.cc'
]
extensions = [
    Extension(
        "zeoplusplus.netstorage",
        sources=netstorage_srcfiles, 
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.geometry", 
        sources=geometry_srcfiles,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.netinfo", 
        sources=netinfo_srcfiles,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.voronoicell",
        sources=voronoicell_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.netio",
        sources=netio_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.graphstorage",
        sources=graphstorage_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.psd",
        sources=psd_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.channel", 
        sources=channel_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.high_accuracy", 
        sources=highaccuracy_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.area_volume", 
        sources=areavol_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.cluster", 
        sources=cluster_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    ),
    Extension(
        "zeoplusplus.cycle", 
        sources=cycle_srcfiles,
        include_dirs=includedirs,
        extra_compile_args=cpp_extra_compile_args,
        language=language
    )
]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name = 'zeoplusplus',
    version = '0.1.0',
    description = "Python interface to Zeo++",
    long_description="Python interface to Zeo++",
    url = "https://github.com/lauri-codes/zeoplusplus",
    author = "Lauri Himanen",
    license = "",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: C++",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
        ],
    # In the Cython build guide it is said that zip_safe should be disabled
    # when building with setuptools
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    ext_modules=extensions,
    keywords="descriptor machine learning atomistic structure materials science",
    python_requires=">=3.6",
)
