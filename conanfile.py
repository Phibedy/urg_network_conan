from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake


class UrgNetworkConan(ConanFile):
    name = "urg_network"
    ZIP_FOLDER_NAME = "urg_library-1.2.0"
    version = "1.2.0"

    def source(self):
        zip_name = "%s.zip" % self.ZIP_FOLDER_NAME
        url = "https://sourceforge.net/projects/urgnetwork/files/urg_library/urg_library-1.2.0.zip/download"
        download(url, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)


    def build(self):
        cmake = CMake(self.settings)
        self.run('cd %s && make'%self.ZIP_FOLDER_NAME)

    def package(self):
        # Copying headers
        self.copy(pattern="*.h", dst="include", src="%s/include" %self.ZIP_FOLDER_NAME, keep_path=True)
        # Copying static and dynamic libs
        self.copy(pattern="*.so", dst="lib", src=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["urg_c","urg_cpp"]
