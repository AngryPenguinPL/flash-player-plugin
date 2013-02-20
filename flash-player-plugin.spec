%ifarch x86_64
%define bitmark	()(64bit)
%else
%define bitmark %nil
%endif

Summary:	Flash Player plugin for browsers
Name:		flash-player-plugin
Version:	11.2.202.270
Release:	1
License:	Proprietary
URL:		http://www.adobe.com/products/flashplayer/
Group:		Networking/WWW
ExclusiveArch:	%ix86 x86_64
Requires(pre):	curl

# helper for getting requires:
# for i in $(objdump -p libflashplayer.so  | grep NEEDED | awk '{ print $2 }' | grep -v ld-linux); do echo "Requires: $i%{bitmark}"; done
Requires:	libatk-1.0.so.0%{bitmark}
Requires:	libcairo.so.2%{bitmark}
Requires:	libc.so.6%{bitmark}
Requires:	libdl.so.2%{bitmark}
Requires:	libfontconfig.so.1%{bitmark}
Requires:	libfreetype.so.6%{bitmark}
Requires:	libgdk_pixbuf-2.0.so.0%{bitmark}
Requires:	libgdk-x11-2.0.so.0%{bitmark}
Requires:	libglib-2.0.so.0%{bitmark}
Requires:	libgmodule-2.0.so.0%{bitmark}
Requires:	libgobject-2.0.so.0%{bitmark}
Requires:	libgthread-2.0.so.0%{bitmark}
Requires:	libgtk-x11-2.0.so.0%{bitmark}
Requires:	libm.so.6%{bitmark}
Requires:	libnspr4.so%{bitmark}
Requires:	libnss3.so%{bitmark}
Requires:	libnssutil3.so%{bitmark}
Requires:	libpango-1.0.so.0%{bitmark}
Requires:	libpangocairo-1.0.so.0%{bitmark}
Requires:	libpangoft2-1.0.so.0%{bitmark}
Requires:	libplc4.so%{bitmark}
Requires:	libplds4.so%{bitmark}
Requires:	libpthread.so.0%{bitmark}
Requires:	librt.so.1%{bitmark}
Requires:	libsmime3.so%{bitmark}
Requires:	libssl3.so%{bitmark}
Requires:	libX11.so.6%{bitmark}
Requires:	libXcursor.so.1%{bitmark}
Requires:	libXext.so.6%{bitmark}
Requires:	libXrender.so.1%{bitmark}
Requires:	libXt.so.6%{bitmark}
# end of helper produced requires

# required for audio, dlopened:
Requires:	libasound.so.2%{bitmark}
# dlopened:
Requires:	libcurl.so.4%{bitmark}
# dlopened, for video acceleration:
Suggests:	libvdpau.so.1%{bitmark}
#
Conflicts:	FlashPlayer < 9.0.115.0-5
Conflicts:	flash-plugin 
Conflicts:	FlashPlayer-plugin
Conflicts:	flashplayer-plugin
# Conflict with free plugins to avoid user confusion as to which one is
# actually used:
Conflicts:	gnash-firefox-plugin
Conflicts:	swfdec-mozilla
Conflicts:	lightspark-mozilla-plugin
Conflicts:	libflashsupport < 0.20080000.1
Obsoletes:	flash-player-plugin10.2 < 10.2.152
Provides:	flash-player-plugin11
Obsoletes:	flash-player-plugin11 < %{version}
BuildRequires:	kde4-macros

%description
Adobe Flash Player plugin for browsers.

NOTE: This package does not contain the Flash Player itself. The
software will be automatically downloaded from Adobe during package
installation.

Installing this package indicates acceptance of the Flash Player EULA,
available at http://www.adobe.com/products/eulas/players/flash/
%ifnarch x86_64
and as %{_libdir}/mozilla/plugins/LICENSE.flashplayer.
%endif

# It would be preferable to have the KCM module in the main package with
# simply not requiring any kde stuff. However, standard KDE installation
# doesn't necessary include libkutils4. - Anssi 08/2011
%package kde
Summary:	Flash Player KDE settings module
Group:		Networking/WWW
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{name} = %{version}-%{release}
# helper for getting requires:
# for i in $(objdump -p kcm_adobe_flash_player.so  | grep NEEDED | awk '{ print $2 }' | grep -v ld-linux); do echo "Requires: $i%{bitmark}"; done
Requires:	libc.so.6%{bitmark}
Requires:	libICE.so.6%{bitmark}
Requires:	libkdecore.so.5%{bitmark}
Requires:	libkdeui.so.5%{bitmark}
Requires:	libkutils.so.4%{bitmark}
Requires:	libm.so.6%{bitmark}
Requires:	libpthread.so.0%{bitmark}
Requires:	libQtCore.so.4%{bitmark}
Requires:	libQtDBus.so.4%{bitmark}
Requires:	libQtGui.so.4%{bitmark}
Requires:	libQtSvg.so.4%{bitmark}
Requires:	libSM.so.6%{bitmark}
Requires:	libX11.so.6%{bitmark}
Requires:	libXau.so.6%{bitmark}
Requires:	libXdmcp.so.6%{bitmark}
Requires:	libXext.so.6%{bitmark}
Requires:	libXft.so.2%{bitmark}
Requires:	libXpm.so.4%{bitmark}
# end of helper produced requires
Conflicts:	flash-player-plugin < 10.3.183.5
Provides:	flash-player-plugin11-kde
Obsoletes:	flash-player-plugin11-kde < %{version}

%description kde
KDE settings module for Adobe Flash Player.

NOTE: This package does not contain the software itself. The
software will be automatically downloaded from the Adobe server
during package installation.

Installing this package indicates acceptance of the Flash Player EULA,
available at http://www.adobe.com/products/eulas/players/flash/
%ifnarch x86_64
and as %{_libdir}/mozilla/plugins/LICENSE.flashplayer.
%endif

%prep
%setup -c -T

# Always prefer versioned archives instead of unversioned ones, so that when
# Adobe updates the Flash Player, the old md5sum continues to work until
# this package is updated for the new version.

# The linuxdownload.adobe.com rpm usually stays up longer, but fpdownload.macromedia.com is faster.
# Their md5sums usually differ.

%ifarch %ix86
%define downurl1	http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/flash-plugin-%{version}-release.i386.rpm
%define tmd5sum1	9e78a36f26a071b9d92581e5245a741c
%define downurl2	http://linuxdownload.adobe.com/linux/i386/flash-plugin-%{version}-release.i386.rpm
%define tmd5sum2	9e78a36f26a071b9d92581e5245a741c
%define downurl3	%nil
%define tmd5sum3	%nil
%define tarname		flash-plugin-%{version}-release.i386.rpm

%define warn_on_missing_files 1
%endif

%ifarch x86_64
%define downurl1	http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/flash-plugin-%{version}-release.x86_64.rpm
%define tmd5sum1	0a01991d6236908d30e771ce6daf4b88
%define downurl2	http://linuxdownload.adobe.com/linux/x86_64/flash-plugin-%{version}-release.x86_64.rpm
%define tmd5sum2	0a01991d6236908d30e771ce6daf4b88
%define downurl3	%nil
%define downurl3	%nil
%define tarname		flash-plugin-%{version}-release.x86_64.rpm

%define warn_on_missing_files 1
%endif

%define file %{_localstatedir}/lib/%{name}/%{tarname}

%install

install -d -m755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m755 %{buildroot}%{_libdir}/mozilla/plugins
touch %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so
touch %{buildroot}%{_libdir}/mozilla/plugins/LICENSE.flashplayer 	 
touch %{buildroot}%{_libdir}/mozilla/plugins/README.flashplayer
touch %{buildroot}%{_localstatedir}/lib/%{name}/%{tarname}

install -d -m755 %{buildroot}%{_bindir}
touch %{buildroot}%{_bindir}/flash-player-properties

install -d -m755 %{buildroot}%{_kde_services}
touch %{buildroot}%{_kde_services}/kcm_adobe_flash_player.desktop
install -d -m755 %{buildroot}%{_kde_libdir}/kde4
touch %{buildroot}%{_kde_libdir}/kde4/kcm_adobe_flash_player.so

install -d -m755 %{buildroot}%{_datadir}/applications
touch %{buildroot}%{_datadir}/applications/flash-player-properties.desktop

for i in 16 22 24 32 48; do
	install -d -m755 %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps
	touch %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/flash-player-properties.png
done

install -d -m755 %{buildroot}%{_datadir}/%{name}
cat > %{buildroot}%{_datadir}/%{name}/functions << EOF
next_file() {
	FILENUM=\$((FILENUM+1))
	eval FILE_SRC="\\\$FILE\${FILENUM}_SRC"
	eval FILE_DST="\\\$FILE\${FILENUM}_DST"
	eval FILE_PRM="\\\$FILE\${FILENUM}_PRM"
	[ -n "\$FILE_SRC" ]
}

tar_extract() {
        extractdir=\$(mktemp -d --tmpdir=/tmp)
	if [ -z "\$extractdir" ]; then
		echo "Error during extraction." >&2
		exit 1
	fi

	cd "\$extractdir" || exit 1

	if [ "\$(head -c4 "%file")" = \$'\\xED\\xAB\\xEE\\xDB' ]; then
		rpm2cpio "%file" | cpio -i --quiet -d -R root:root
	else
		tar -xzf "%file" --no-same-owner --no-same-permissions
	fi

	# Avoid leaving old files in case of failure below
	FILENUM=0
	while next_file; do
		rm -f "\$FILE_DST"
	done

	FILENUM=0
	while next_file; do
		if [ ! -f "\$FILE_SRC" ]; then
%if %warn_on_missing_files
			echo "Warning: \$FILE_SRC not found in the Flash Player archive," >&2
			echo "         skipping installation of \$FILE_DST." >&2
			echo "         Please file a bug report at https://openmandriva.org/ ." >&2
%endif
			continue
		fi
			
		chmod "\$FILE_PRM" "\$FILE_SRC"
		mv -f "\$FILE_SRC" "\$FILE_DST"
	done
	rm -rf "\$extractdir"
}
EOF

%pre
checkmd5sum() {
	[ -e "$1" ] || return 1
	FILEMD5="$(md5sum $1 | cut -d" " -f1)"
	[ -n "$FILEMD5" ] || return 1
	MD5NUM=1
	eval MD5SUM="\$MD5SUM$MD5NUM"
	while [ "$MD5SUM" ]; do
		[ "$MD5SUM" = "$FILEMD5" ] && return 0
		MD5NUM=$((MD5NUM+1))
		eval MD5SUM="\$MD5SUM$MD5NUM"
	done
	return 1
}

get_proxy_from_urpmi() {
	if [ -e /etc/urpmi/proxy.cfg ]; then
		proxy="$(grep ^http_proxy= /etc/urpmi/proxy.cfg 2>/dev/null)"
		proxy_user="$(grep ^proxy_user= /etc/urpmi/proxy.cfg 2>/dev/null)"

		proxy="${proxy#http_proxy=}"
		proxy_user="${proxy_user#proxy_user=}"

		[ -n "$proxy" ] && echo "--proxy $proxy"
		[ -n "$proxy_user" ] && echo "--proxy-user $proxy_user"
	fi
}

MD5SUM1="%{tmd5sum1}"
MD5SUM2="%{tmd5sum2}"
MD5SUM3="%{tmd5sum3}"
MD5SUM4=
URL1="%{downurl1}"
URL2="%{downurl2}"
URL3="%{downurl3}"
URL4=

URLNUM=1

install -d -m 0755 %{_localstatedir}/lib/%{name}

echo "Note that by downloading the Adobe Flash Player you indicate your acceptance of"
echo "the EULA, available at http://www.adobe.com/products/eulas/players/flash/"
while ! checkmd5sum "%file"; do
	eval URL="\$URL$URLNUM"
	if [ -z "$URL" ]; then
		echo "Error: Unable to download Flash Player. This is likely due to this package" >&2
		echo "       being too old. Please file a bug report at https://openmandriva.org" >&2
		echo "       so that the package gets updated. Thank you." >&2
		echo "" >&2
		echo "       In the meantime, you can download Flash Player manually from" >&2
		echo "       http://get.adobe.com/flashplayer/" >&2
		rm -f "%file"
		[ "$(ls -A "%{_localstatedir}/lib/%{name}")" ] && rm -rf "%{_localstatedir}/lib/%{name}"
		exit 1
	fi
	URLNUM=$((URLNUM+1))
	echo "Downloading from $URL:"
	curl --connect-timeout 20 -m 10800 -L $(get_proxy_from_urpmi) "$URL" > "%file"
done

%post
FILE1_SRC="usr/%{_lib}/flash-plugin/libflashplayer.so"
FILE1_DST="%{_libdir}/mozilla/plugins/libflashplayer.so"
FILE1_PRM="0755"
FILE2_SRC="usr/%{_lib}/flash-plugin/LICENSE"
FILE2_DST="%{_libdir}/mozilla/plugins/LICENSE.flashplayer"
FILE2_PRM="0644"
FILE3_SRC="usr/%{_lib}/flash-plugin/README"
FILE3_DST="%{_libdir}/mozilla/plugins/README.flashplayer"
FILE3_PRM="0644"

FILE4_SRC="usr/bin/flash-player-properties"
FILE4_DST="%{_bindir}/flash-player-properties"
FILE4_PRM="0755"
FILE5_SRC="usr/share/applications/flash-player-properties.desktop"
FILE5_DST="%{_datadir}/applications/flash-player-properties.desktop"
FILE5_PRM="0644"

FILE6_SRC="usr/share/icons/hicolor/16x16/apps/flash-player-properties.png"
FILE6_DST="%{_iconsdir}/hicolor/16x16/apps/flash-player-properties.png"
FILE6_PRM="0644"
FILE7_SRC="usr/share/icons/hicolor/22x22/apps/flash-player-properties.png"
FILE7_DST="%{_iconsdir}/hicolor/22x22/apps/flash-player-properties.png"
FILE7_PRM="0644"
FILE8_SRC="usr/share/icons/hicolor/24x24/apps/flash-player-properties.png"
FILE8_DST="%{_iconsdir}/hicolor/24x24/apps/flash-player-properties.png"
FILE8_PRM="0644"
FILE9_SRC="usr/share/icons/hicolor/32x32/apps/flash-player-properties.png"
FILE9_DST="%{_iconsdir}/hicolor/32x32/apps/flash-player-properties.png"
FILE9_PRM="0644"
FILE10_SRC="usr/share/icons/hicolor/48x48/apps/flash-player-properties.png"
FILE10_DST="%{_iconsdir}/hicolor/48x48/apps/flash-player-properties.png"
FILE10_PRM="0644"
FILE11_SRC=

. %{_datadir}/%{name}/functions
tar_extract

# show in KDE as well (in case user doesn't have -kde subpkg
sed -i 's,NotShowIn=KDE;,,' %{_datadir}/applications/flash-player-properties.desktop 2>/dev/null || :
# otherwise KDE hides it:
sed -i 's,GNOME;,,' %{_datadir}/applications/flash-player-properties.desktop 2>/dev/null || :

echo "Adobe Flash Player installation successful."

%pre kde
# When installing both main package and -kde, failure of %pre of main package
# can prevent installation of it, but urpmi/rpm will try to install -kde
# regardless. FIXME.
# For now, workaround it by preventing -kde installation as well:
[ -e %{_datadir}/%{name}/functions ]

%post kde
FILE1_SRC="usr/%{_lib}/kde4/kcm_adobe_flash_player.so"
FILE1_DST="%{_kde_libdir}/kde4/kcm_adobe_flash_player.so"
FILE1_PRM="0755"
FILE2_SRC="usr/share/kde4/services/kcm_adobe_flash_player.desktop"
FILE2_DST="%{_kde_services}/kcm_adobe_flash_player.desktop"
FILE2_PRM="0644"
FILE3_SRC=

. %{_datadir}/%{name}/functions
tar_extract

sed -i 's,=personal,=network-and-connectivity,' %{_kde_services}/kcm_adobe_flash_player.desktop 2>/dev/null || :

%files
%dir %{_localstatedir}/lib/%{name}
%ghost %{_localstatedir}/lib/%{name}/%{tarname}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/functions

%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%ghost %{_libdir}/mozilla/plugins/libflashplayer.so
%ghost %{_libdir}/mozilla/plugins/LICENSE.flashplayer
%ghost %{_libdir}/mozilla/plugins/README.flashplayer

%ghost %{_bindir}/flash-player-properties
%ghost %{_datadir}/applications/flash-player-properties.desktop
%ghost %{_iconsdir}/hicolor/*/apps/flash-player-properties.png

%files kde
%ghost %{_kde_libdir}/kde4/kcm_adobe_flash_player.so
%ghost %{_kde_services}/kcm_adobe_flash_player.desktop


%changelog

* Tue Oct 09 2012 anssi <anssi> 11.2.202.243-1.mga2
+ Revision: 303970
- new version 11.2.202.243
  o fixes CVE-2012-5248, CVE-2012-5249, CVE-2012-5250, CVE-2012-5251,
    CVE-2012-5252, CVE-2012-5253, CVE-2012-5254, CVE-2012-5255, CVE-2012-5256,
    CVE-2012-5257, CVE-2012-5258, CVE-2012-5259, CVE-2012-5260, CVE-2012-5261,
    CVE-2012-5262, CVE-2012-5263, CVE-2012-5264, CVE-2012-5265, CVE-2012-5266,
    CVE-2012-5267, CVE-2012-5268, CVE-2012-5269, CVE-2012-5270, CVE-2012-5271,
    CVE-2012-5272
    (bulletin: http://www.adobe.com/support/security/bulletins/apsb12-22.html )

* Sun Aug 19 2012 anssi <anssi> 11.2.202.238-1.mga2.nonfree
+ Revision: 282318
- new version 11.2.202.238
  o fixes a critical security vulnerability (CVE-2012-1535,
    http://www.adobe.com/support/security/bulletins/apsb12-18.html )

* Sat Jun 09 2012 anssi <anssi> 11.2.202.236-1.mga2.nonfree
+ Revision: 258425
- new version 11.2.202.236
  o fixes critical security vulnerabilities (CVE-2012-2034, CVE-2012-2035,
    CVE-2012-2036, CVE-2012-2037, CVE-2012-2038, CVE-2012-2039,
    CVE-2012-2040,
    http://www.adobe.com/support/security/bulletins/apsb12-14.html )
- require libraries by file names instead of package names (suggested
  by simplew, fixes #5824 (unable to use libcairo-xcb2))
- 11.2.202.235
  o fixes security issue CVE-2012-0779
    (http://www.adobe.com/support/security/bulletins/apsb12-09.html)

* Tue Apr 17 2012 anssi <anssi> 11.2.202.233-1.mga2.nonfree
+ Revision: 231210
- new version 11.2.202.233
  o bugfixes related to stability and performance
- add some more direct requirements (they were also satisfied
  indirectly via GTK+)

* Thu Mar 29 2012 anssi <anssi> 11.2.202.228-1.mga2.nonfree
+ Revision: 227535
- new version 11.2.202.228
  o fixes a memory corruption vulnerability (CVE-2012-0773)

* Tue Mar 06 2012 anssi <anssi> 11.1.102.63-1.mga2.nonfree
+ Revision: 220477
- new version 11.1.102.63
  o fixes CVE-2012-0768, CVE-2012-0769
    ( http://www.adobe.com/support/security/bulletins/apsb12-05.html )

* Fri Feb 17 2012 anssi <anssi> 11.1.102.62-1.mga2.nonfree
+ Revision: 210094
- new version
  o fixes CVE-2012-0751, CVE-2012-0752, CVE-2012-0753, CVE-2012-0754,
    CVE-2012-0755, CVE-2012-0756, CVE-2012-0767

* Fri Dec 16 2011 anssi <anssi> 11.1.102.55-2.mga2.nonfree
+ Revision: 182382
- use proxy settings from /etc/urpmi/proxy.cfg (bug #3044)

* Fri Nov 11 2011 anssi <anssi> 11.1.102.55-1.mga2.nonfree
+ Revision: 166427
- new version 11.1.102.55
  o fixes overflow and corruption vulnerabilities CVE-2011-2445,
    CVE-2011-2450, CVE-2011-2451, CVE-2011-2452, CVE-2011-2453,
    CVE-2011-2454, CVE-2011-2455, CVE-2011-2456, CVE-2011-2457,
    CVE-2011-2459, CVE-2011-2460
- normal download used again for x86_64, upstream issue regarding
  missing files was fixed
- prevent installation of -kde in %%pre if main package installation
  was prevented by its %%pre

* Thu Oct 06 2011 anssi <anssi> 11.0.1.152-1.mga2.nonfree
+ Revision: 152244
- prefer unversioned archive on x86_64 (for now), fallbacking to the
  versioned one, since the latter one misses some files

  + doktor5000 <doktor5000>
    - new version 11.0 final
    - obsolete flash-player-plugin11
    - remove fake x86_64 stuff, provide native x86_64 plugin
    - remove Require for nspluginwrapper
    - remove obsolete empty %%defattr and %%_localstatedir

* Thu Sep 22 2011 anssi <anssi> 10.3.183.10-1.mga2.nonfree
+ Revision: 146583
- new version 10.3.183.10
  o fixes CVE-2011-2426, CVE-2011-2427, CVE-2011-2428, CVE-2011-2429
    CVE-2011-2430, CVE-2011-2444
- enforce permissions for extracted files (no effect with current
  Flash Player version)
- new version 10.3.183.7
- clean up on download failure
- provide a fake 64-bit version of the package which installs the
  32-bit version of the Flash Player, to make the installation easier
  on 64-bit installations that do not have 32-bit nonfree repository
  set up by default; the package will be automatically upgraded to
  a true 64-bit stable Flash Player when it becomes available
- split out KDE KCM module into -kde subpackage (bug #1275)
- download in %%pre instead of %%posttrans
- unpack in %%post instead of %%posttrans
- always re-enable GTK flash-player-properties in KDE as well
- drop now unneeded calls to nspluginwrapper and gtk-icon-cache,
  they are now handled by filetriggers
- new version

  + ahmad <ahmad>
    - Change references of PLF to Mageia in download-flash-player-plugin

* Fri Jul 08 2011 ahmad <ahmad> 10.3.181.34-1.mga2.nonfree
+ Revision: 120127
- Update to 10.3.181.34

* Wed Jun 15 2011 ahmad <ahmad> 10.3.181.26-1.mga2.nonfree
+ Revision: 107959
- Update to 10.3.181.26

* Thu Jun 09 2011 ahmad <ahmad> 10.3.181.22-1.mga2.nonfree
+ Revision: 102309
- Update to 10.3.181.22

* Fri May 13 2011 anssi <anssi> 10.3.181.14-1.mga1
+ Revision: 98265
- new version
- adapt script for added files
- 32bit KDE now has a settings applet in KDE System Settings, other desktops
  (including 64bit KDE) have a standalone configuration application

* Wed Apr 20 2011 ennael <ennael> 10.2.159.1-1.mga1
+ Revision: 89107
- imported package flash-player-plugin

