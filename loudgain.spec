Version: 0.6.8
%global forgeurl https://github.com/Moonbase59/loudgain
%forgemeta

Name: %{repo}
Release: 1%{?dist}
Summary: ReplayGain 2.0 audio loudness normalizer
License: BSD
URL: %{forgeurl}
Source0: %{forgesource}

# https://github.com/Moonbase59/loudgain/pull/37
Patch0: hardened-build.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ffmpeg-devel
BuildRequires: libebur128-devel
BuildRequires: taglib-devel


%description
loudgain is a versatile ReplayGain 2.0 loudness normalizer, based on the
EBU R128/ITU BS.1770 standard (-18 LUFS) and supports
FLAC/Ogg/MP2/MP3/MP4/M4A/ALAC/Opus/ASF/WMA/WAV/WavPack/AIFF/APE audio
files. It uses the well-known mp3gain commandline syntax but will never
modify the actual audio data.


%prep
%forgeautosetup


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/rgbpm
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Oct 19 2020 Peter Oliver <rpm@mavit.org.uk> - 0.6.8-1
- Initial package.
