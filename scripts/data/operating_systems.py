"""Notable operating systems."""

META = {
    "name": "operating-systems",
    "title": "Operating Systems",
    "description": "Notable operating systems with their family, developer, and kernel.",
    "emoji": "\U0001F4BB",
}

# id, name, family, first_release_year, developer, kernel
_RAW = [
    ("unix", "Unix", "Unix", 1969, "Bell Labs", None),
    ("windows-95", "Windows 95", "Windows", 1995, "Microsoft", None),
    ("windows-xp", "Windows XP", "Windows", 2001, "Microsoft", "Windows NT"),
    ("windows-7", "Windows 7", "Windows", 2009, "Microsoft", "Windows NT"),
    ("windows-10", "Windows 10", "Windows", 2015, "Microsoft", "Windows NT"),
    ("windows-11", "Windows 11", "Windows", 2021, "Microsoft", "Windows NT"),
    ("ms-dos", "MS-DOS", "Other", 1981, "Microsoft", None),
    ("macos", "macOS", "macOS", 2001, "Apple", "XNU"),
    ("mac-os-classic", "Mac OS (Classic)", "Other", 1984, "Apple", None),
    ("linux", "Linux", "Linux", 1991, "Linus Torvalds", "Linux"),
    ("ubuntu", "Ubuntu", "Linux", 2004, "Canonical", "Linux"),
    ("debian", "Debian", "Linux", 1993, "Debian Project", "Linux"),
    ("fedora", "Fedora", "Linux", 2003, "Red Hat", "Linux"),
    ("red-hat-enterprise-linux", "Red Hat Enterprise Linux", "Linux", 2000, "Red Hat", "Linux"),
    ("arch-linux", "Arch Linux", "Linux", 2002, "Arch Linux", "Linux"),
    ("android", "Android", "Mobile", 2008, "Google", "Linux"),
    ("ios", "iOS", "Mobile", 2007, "Apple", "XNU"),
    ("freebsd", "FreeBSD", "BSD", 1993, "FreeBSD Project", "FreeBSD"),
    ("openbsd", "OpenBSD", "BSD", 1996, "OpenBSD Project", "OpenBSD"),
    ("netbsd", "NetBSD", "BSD", 1993, "NetBSD Foundation", "NetBSD"),
    ("solaris", "Solaris", "Unix", 1992, "Sun Microsystems", "SunOS"),
    ("chrome-os", "ChromeOS", "Linux", 2011, "Google", "Linux"),
    ("os-2", "OS/2", "Other", 1987, "IBM and Microsoft", None),
    ("beos", "BeOS", "Other", 1995, "Be Inc.", None),
    ("haiku", "Haiku", "Other", 2009, "Haiku Inc.", "Haiku kernel"),
    ("amigaos", "AmigaOS", "Other", 1985, "Commodore", "Exec"),
]

ITEMS = [
    {
        "id": _id,
        "name": name,
        "family": family,
        "first_release_year": year,
        "developer": developer,
        "kernel": kernel,
    }
    for _id, name, family, year, developer, kernel in _RAW
]
