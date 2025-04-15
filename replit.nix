{pkgs}: {
  deps = [
    pkgs.libxcrypt
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.pkg-config
    pkgs.arrow-cpp
    pkgs.google-cloud-sdk-gce
    pkgs.bash
    pkgs.nodePackages.prettier
    pkgs.lsof
  ];
}
