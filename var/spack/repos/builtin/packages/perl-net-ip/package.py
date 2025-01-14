# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2023 EMBL-European Bioinformatics Institute
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlNetIp(PerlPackage):
    """Perl extension for manipulating IPv4/IPv6 addresses"""

    homepage = "https://metacpan.org/pod/Net::IP"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MANU/Net-IP-1.26.tar.gz"

    maintainers("EbiArnie")

    version("1.26", sha256="040f16f3066647d761b724a3b70754d28cbd1e6fe5ea01c63ed1cd857117d639")

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use Net::IP; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
