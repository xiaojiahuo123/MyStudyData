# Ubuntu 22.04 虚拟机 syslog 日志

- **来源**: /var/log/syslog
- **主机**: ty-virtual-machine
- **系统**: Ubuntu 22.04.4 LTS (Jammy Jellyfish)
- **内核**: 6.5.0-18-generic
- **导出时间**: 2026-06-30

---

## 日志内容

```syslog
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] Linux version 6.5.0-18-generic (buildd@lcy02-amd64-070) (x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #18~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Feb  7 11:40:03 UTC 2 (Ubuntu 6.5.0-18.18~22.04.1-generic 6.5.8)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic root=UUID=4a64a517-67dd-4c66-898a-7aec80564857 ro find_preseed=/preseed.cfg auto noprompt priority=critical locale=en_US quiet splash
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] KERNEL supported cpus:
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000]   Intel GenuineIntel
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000]   AMD AuthenticAMD
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000]   Hygon HygonGenuine
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000]   Centaur CentaurHauls
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000]   zhaoxin   Shanghai  
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-provided physical RAM map:
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009e7ff] usable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x000000000009e800-0x000000000009ffff] reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000000dc000-0x00000000000fffff] reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000bfecffff] usable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000bfed0000-0x00000000bfefefff] ACPI data
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000bfeff000-0x00000000bfefffff] ACPI NVS
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000bff00000-0x00000000bfffffff] usable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000f0000000-0x00000000f7ffffff] reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec0ffff] reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000fffe0000-0x00000000ffffffff] reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000013fffffff] usable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] NX (Execute Disable) protection: active
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] SMBIOS 2.7 present.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] DMI: VMware, Inc. VMware Virtual Platform/440BX Desktop Reference Platform, BIOS 6.00 11/12/2020
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] vmware: hypercall mode: 0x02
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] Hypervisor detected: VMware
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] vmware: TSC freq read from hypervisor : 2419.202 MHz
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] vmware: Host bus clock speed read from hypervisor : 66000000 Hz
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000000] vmware: using clock offset of 6082428089 ns
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.000043] tsc: Detected 2419.202 MHz processor
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.003700] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.003715] e820: remove [mem 0x000a0000-0x000fffff] usable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.003730] last_pfn = 0x140000 max_arch_pfn = 0x400000000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.003799] total RAM covered: 130048M
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.004105] Found optimal setting for mtrr clean up
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.004106]  gran_size: 64K 	chunk_size: 64K 	num_reg: 7  	lose cover RAM: 0G
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.004115] MTRR map: 7 entries (5 fixed + 2 variable; max 21), built from 8 variable MTRRs
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.004121] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.004273] e820: update [mem 0xc0000000-0xffffffff] usable ==> reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.004290] last_pfn = 0xc0000 max_arch_pfn = 0x400000000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.012928] found SMP MP-table at [mem 0x000f6a70-0x000f6a7f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.012988] Using GB pages for direct mapping
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.012990] Incomplete global flushes, disabling PCID
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013631] RAMDISK: [mem 0x2fa09000-0x33cfbfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013646] ACPI: Early table checksum verification disabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013654] ACPI: RSDP 0x00000000000F6A00 000024 (v02 PTLTD )
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013663] ACPI: XSDT 0x00000000BFEDC633 00005C (v01 INTEL  440BX    06040000 VMW  01324272)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013674] ACPI: FACP 0x00000000BFEFEE73 0000F4 (v04 INTEL  440BX    06040000 PTL  000F4240)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013685] ACPI: DSDT 0x00000000BFEDD9E8 02148B (v01 PTLTD  Custom   06040000 MSFT 03000001)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013698] ACPI: FACS 0x00000000BFEFFFC0 000040
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013704] ACPI: FACS 0x00000000BFEFFFC0 000040
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013709] ACPI: BOOT 0x00000000BFEDD9C0 000028 (v01 PTLTD  $SBFTBL$ 06040000  LTP 00000001)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013714] ACPI: APIC 0x00000000BFEDD27E 000742 (v01 PTLTD  ? APIC   06040000  LTP 00000000)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013719] ACPI: MCFG 0x00000000BFEDD242 00003C (v01 PTLTD  $PCITBL$ 06040000  LTP 00000001)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013725] ACPI: SRAT 0x00000000BFEDC72F 0008D0 (v02 VMWARE MEMPLUG  06040000 VMW  00000001)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013730] ACPI: HPET 0x00000000BFEDC6F7 000038 (v01 VMWARE VMW HPET 06040000 VMW  00000001)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013735] ACPI: WAET 0x00000000BFEDC6CF 000028 (v01 VMWARE VMW WAET 06040000 VMW  00000001)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013739] ACPI: Reserving FACP table memory at [mem 0xbfefee73-0xbfefef66]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013742] ACPI: Reserving DSDT table memory at [mem 0xbfedd9e8-0xbfefee72]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013744] ACPI: Reserving FACS table memory at [mem 0xbfefffc0-0xbfefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013746] ACPI: Reserving FACS table memory at [mem 0xbfefffc0-0xbfefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013747] ACPI: Reserving BOOT table memory at [mem 0xbfedd9c0-0xbfedd9e7]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013749] ACPI: Reserving APIC table memory at [mem 0xbfedd27e-0xbfedd9bf]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013750] ACPI: Reserving MCFG table memory at [mem 0xbfedd242-0xbfedd27d]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013752] ACPI: Reserving SRAT table memory at [mem 0xbfedc72f-0xbfedcffe]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013753] ACPI: Reserving HPET table memory at [mem 0xbfedc6f7-0xbfedc72e]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013754] ACPI: Reserving WAET table memory at [mem 0xbfedc6cf-0xbfedc6f6]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013835] system APIC only can use physical flat
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013837] Setting APIC routing to physical flat.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013931] SRAT: PXM 0 -> APIC 0x00 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013935] SRAT: PXM 0 -> APIC 0x01 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013936] SRAT: PXM 0 -> APIC 0x02 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013938] SRAT: PXM 0 -> APIC 0x03 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013939] SRAT: PXM 0 -> APIC 0x04 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013940] SRAT: PXM 0 -> APIC 0x05 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013942] SRAT: PXM 0 -> APIC 0x06 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013943] SRAT: PXM 0 -> APIC 0x07 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013944] SRAT: PXM 0 -> APIC 0x08 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013946] SRAT: PXM 0 -> APIC 0x09 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013947] SRAT: PXM 0 -> APIC 0x0a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013948] SRAT: PXM 0 -> APIC 0x0b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013949] SRAT: PXM 0 -> APIC 0x0c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013951] SRAT: PXM 0 -> APIC 0x0d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013952] SRAT: PXM 0 -> APIC 0x0e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013953] SRAT: PXM 0 -> APIC 0x0f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013955] SRAT: PXM 0 -> APIC 0x10 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013956] SRAT: PXM 0 -> APIC 0x11 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013958] SRAT: PXM 0 -> APIC 0x12 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013959] SRAT: PXM 0 -> APIC 0x13 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013960] SRAT: PXM 0 -> APIC 0x14 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013962] SRAT: PXM 0 -> APIC 0x15 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013963] SRAT: PXM 0 -> APIC 0x16 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013964] SRAT: PXM 0 -> APIC 0x17 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013965] SRAT: PXM 0 -> APIC 0x18 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013967] SRAT: PXM 0 -> APIC 0x19 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013968] SRAT: PXM 0 -> APIC 0x1a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013969] SRAT: PXM 0 -> APIC 0x1b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013971] SRAT: PXM 0 -> APIC 0x1c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013972] SRAT: PXM 0 -> APIC 0x1d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013973] SRAT: PXM 0 -> APIC 0x1e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013975] SRAT: PXM 0 -> APIC 0x1f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013976] SRAT: PXM 0 -> APIC 0x20 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013977] SRAT: PXM 0 -> APIC 0x21 -> Node 0
Jun 30 05:29:39 ty-virtual-machine systemd-modules-load[346]: Inserted module 'lp'
Jun 30 05:29:39 ty-virtual-machine systemd-modules-load[346]: Inserted module 'ppdev'
Jun 30 05:29:39 ty-virtual-machine systemd-modules-load[346]: Inserted module 'parport_pc'
Jun 30 05:29:39 ty-virtual-machine systemd-modules-load[346]: Inserted module 'msr'
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Apply Kernel Variables.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for bare, revision 5.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for core22, revision 1122.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for firefox, revision 3836.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for gnome-42-2204, revision 141.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for gtk-common-themes, revision 1535.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for snap-store, revision 959.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for snapd, revision 20671.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Mount unit for snapd-desktop-integration, revision 83.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Mounted snaps.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Flush Journal to Persistent Storage...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Flush Journal to Persistent Storage.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Coldplug All udev Devices.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Rule-based Manager for Device Events and Files.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Show Plymouth Boot Screen...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Received SIGRTMIN+20 from PID 401 (plymouthd).
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Show Plymouth Boot Screen.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Dispatch Password Requests to Console Directory Watch being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Forward Password Requests to Plymouth Directory Watch.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Local Encrypted Volumes.
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[389]: Using default interface naming scheme 'v249'.
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[400]: sda: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda' failed with exit code 1.
Jun 30 05:29:39 ty-virtual-machine mtp-probe: checking bus 1, device 2: "/sys/devices/pci0000:00/0000:00:11.0/0000:02:00.0/usb1/1-1"
Jun 30 05:29:39 ty-virtual-machine mtp-probe: bus: 1, device: 2 was not an MTP device
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[392]: sda1: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda1' failed with exit code 1.
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[397]: sda3: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda3' failed with exit code 1.
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[390]: fd0: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/fd0' failed with exit code 1.
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[400]: sda2: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda2' failed with exit code 1.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Found device VMware_Virtual_S EFI\x20System\x20Partition.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting File System Check on /dev/disk/by-uuid/9E97-3BEC...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started File System Check Daemon to report status.
Jun 30 05:29:39 ty-virtual-machine systemd-fsck[439]: fsck.fat 4.2 (2021-01-31)
Jun 30 05:29:39 ty-virtual-machine systemd-fsck[439]: /dev/sda2: 11 files, 1555/131063 clusters
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished File System Check on /dev/disk/by-uuid/9E97-3BEC.
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[395]: sr0: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sr0' failed with exit code 1.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounting /boot/efi...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted /boot/efi.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Local File Systems.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Load AppArmor profiles...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Set console font and keymap...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Tell Plymouth To Write Out Runtime Data...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Set Up Additional Binary Formats...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Commit a transient machine-id on disk...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Create Volatile Files and Directories...
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[399]: sr1: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sr1' failed with exit code 1.
Jun 30 05:29:39 ty-virtual-machine apparmor.systemd[450]: Restarting AppArmor
Jun 30 05:29:39 ty-virtual-machine apparmor.systemd[450]: Reloading AppArmor profiles
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Uncomplicated firewall...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Set console font and keymap.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Tell Plymouth To Write Out Runtime Data.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Received SIGRTMIN+20 from PID 401 (plymouthd).
Jun 30 05:29:39 ty-virtual-machine systemd[1]: proc-sys-fs-binfmt_misc.automount: Got automount request for /proc/sys/fs/binfmt_misc, triggered by 458 (systemd-binfmt)
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounting Arbitrary Executable File Formats File System...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Create Volatile Files and Directories.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Uncomplicated firewall.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Preparation for Network.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Userspace Out-Of-Memory (OOM) Killer...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Network Name Resolution...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Network Time Synchronization...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Record System Boot/Shutdown in UTMP...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: etc-machine\x2did.mount: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Commit a transient machine-id on disk.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Mounted Arbitrary Executable File Formats File System.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Set Up Additional Binary Formats.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Record System Boot/Shutdown in UTMP.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Network Time Synchronization.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target System Time Set.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Userspace Out-Of-Memory (OOM) Killer.
Jun 30 05:29:39 ty-virtual-machine systemd-resolved[481]: Positive Trust Anchors:
Jun 30 05:29:39 ty-virtual-machine systemd-resolved[481]: . IN DS 20326 8 2 e06d44b80b8f1d39a95c0b0d7c65d08458e880409bbc683457104237c7f8ec8d
Jun 30 05:29:39 ty-virtual-machine systemd-resolved[481]: Negative trust anchors: home.arpa 10.in-addr.arpa 16.172.in-addr.arpa 17.172.in-addr.arpa 18.172.in-addr.arpa 19.172.in-addr.arpa 20.172.in-addr.arpa 21.172.in-addr.arpa 22.172.in-addr.arpa 23.172.in-addr.arpa 24.172.in-addr.arpa 25.172.in-addr.arpa 26.172.in-addr.arpa 27.172.in-addr.arpa 28.172.in-addr.arpa 29.172.in-addr.arpa 30.172.in-addr.arpa 31.172.in-addr.arpa 168.192.in-addr.arpa d.f.ip6.arpa corp home internal intranet lan local private test
Jun 30 05:29:39 ty-virtual-machine systemd-resolved[481]: Using system hostname 'ty-virtual-machine'.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Network Name Resolution.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Host and Network Name Lookups.
Jun 30 05:29:39 ty-virtual-machine systemd-udevd[376]: controlC0: Process '/usr/sbin/alsactl -E HOME=/run/alsa -E XDG_RUNTIME_DIR=/run/alsa/runtime restore 0' failed with exit code 2.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Dispatch Password Requests to Console Directory Watch being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 30 05:29:39 ty-virtual-machine apparmor.systemd[636]: Skipping profile in /etc/apparmor.d/disable: usr.sbin.rsyslogd
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Load AppArmor profiles.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Load AppArmor profiles managed internally by snapd...
Jun 30 05:29:39 ty-virtual-machine snapd-apparmor[637]: main.go:124: Loading profiles [/var/lib/snapd/apparmor/profiles/snap-confine.snapd.20671 /var/lib/snapd/apparmor/profiles/snap-update-ns.firefox /var/lib/snapd/apparmor/profiles/snap-update-ns.snap-store /var/lib/snapd/apparmor/profiles/snap-update-ns.snapd-desktop-integration /var/lib/snapd/apparmor/profiles/snap.firefox.firefox /var/lib/snapd/apparmor/profiles/snap.firefox.geckodriver /var/lib/snapd/apparmor/profiles/snap.firefox.hook.configure /var/lib/snapd/apparmor/profiles/snap.firefox.hook.connect-plug-host-hunspell /var/lib/snapd/apparmor/profiles/snap.firefox.hook.disconnect-plug-host-hunspell /var/lib/snapd/apparmor/profiles/snap.firefox.hook.post-refresh /var/lib/snapd/apparmor/profiles/snap.snap-store.hook.configure /var/lib/snapd/apparmor/profiles/snap.snap-store.snap-store /var/lib/snapd/apparmor/profiles/snap.snap-store.ubuntu-software /var/lib/snapd/apparmor/profiles/snap.snap-store.ubuntu-software-local-file /var/lib/snapd/apparmor/profiles/snap.snapd-desktop-integration.hook.configure /var/lib/snapd/apparmor/profiles/snap.snapd-desktop-integration.snapd-desktop-integration]
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Load AppArmor profiles managed internally by snapd.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target System Initialization.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started ACPI Events Check.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Process error reports when automatic reporting is enabled (file watch) being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started CUPS Scheduler.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Start whoopsie on modification of the /var/crash directory.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Trigger anacron every hour.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Process error reports when automatic reporting is enabled (timer based) being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Daily apt download activities.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Daily apt upgrade and clean activities.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Daily dpkg database backup timer.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Periodic ext4 Online Metadata Check for All Filesystems.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Discard unused blocks once a week.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Refresh fwupd metadata regularly.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Daily rotation of log files.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Daily man-db regeneration.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Message of the Day.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Timer to automatically fetch and run repair assertions being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Daily Cleanup of Temporary Directories.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Ubuntu Pro Timer for running repeated jobs being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Path Units.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Listening on ACPID Listen Socket.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Unix socket for apport crash forwarding being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Listening on CUPS Scheduler.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Listening on D-Bus System Message Bus Socket.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Socket activation for snappy daemon...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Listening on UUID daemon activation socket.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Listening on Socket activation for snappy daemon.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Socket Units.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Basic System.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Accounts Service...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started ACPI event daemon.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Run anacron jobs.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting LSB: automatic crash report generation...
Jun 30 05:29:39 ty-virtual-machine anacron[669]: Anacron 2.3 started on 2026-06-30
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Avahi mDNS/DNS-SD Stack...
Jun 30 05:29:39 ty-virtual-machine anacron[669]: Will run job `cron.daily' in 5 min.
Jun 30 05:29:39 ty-virtual-machine anacron[669]: Will run job `cron.weekly' in 10 min.
Jun 30 05:29:39 ty-virtual-machine anacron[669]: Will run job `cron.monthly' in 15 min.
Jun 30 05:29:39 ty-virtual-machine anacron[669]: Jobs will be executed sequentially
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Regular background program processing daemon.
Jun 30 05:29:39 ty-virtual-machine cron[672]: (CRON) INFO (pidfile fd = 3)
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started D-Bus System Message Bus.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Network Manager...
Jun 30 05:29:39 ty-virtual-machine cron[672]: (CRON) INFO (Running @reboot jobs)
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Found user 'avahi' (UID 114) and group 'avahi' (GID 121).
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Save initial kernel messages after boot.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Remove Stale Online ext4 Metadata Check Snapshots...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in getty on tty2-tty6 if dbus and logind are not available being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Login Prompts.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Detect the available GPUs and deal with any system changes...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Record successful boot for GRUB...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started irqbalance daemon.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Dispatcher daemon for systemd-networkd...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Authorization Manager...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Power Profiles daemon...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting System Logging Service...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Secure Boot updates for DB and DBX being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Userspace listener for prompt events.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Automatically repair incorrect owner/permissions on core devices being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Wait for the Ubuntu Core chooser trigger being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Preparation for Logins.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Snap Daemon...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Switcheroo Control Proxy service...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting User Login Management...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Thermal Daemon Service being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Ubuntu Pro reboot cmds being skipped.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Disk Manager...
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: dbus[674]: Unknown group "power" in message bus configuration file
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting WPA supplicant...
Jun 30 05:29:39 ty-virtual-machine rsyslogd: imuxsock: Acquired UNIX socket '/run/systemd/journal/syslog' (fd 3) from systemd.  [v8.2112.0]
Jun 30 05:29:39 ty-virtual-machine rsyslogd: rsyslogd's groupid changed to 111
Jun 30 05:29:39 ty-virtual-machine rsyslogd: rsyslogd's userid changed to 104
Jun 30 05:29:39 ty-virtual-machine rsyslogd: [origin software="rsyslogd" swVersion="8.2112.0" x-pid="690" x-info="https://www.rsyslog.com"] start
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Successfully dropped root privileges.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: avahi-daemon 0.8 starting up.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started System Logging Service.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013978] SRAT: PXM 0 -> APIC 0x22 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013980] SRAT: PXM 0 -> APIC 0x23 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013981] SRAT: PXM 0 -> APIC 0x24 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013982] SRAT: PXM 0 -> APIC 0x25 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013984] SRAT: PXM 0 -> APIC 0x26 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013985] SRAT: PXM 0 -> APIC 0x27 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013986] SRAT: PXM 0 -> APIC 0x28 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013988] SRAT: PXM 0 -> APIC 0x29 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013989] SRAT: PXM 0 -> APIC 0x2a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013990] SRAT: PXM 0 -> APIC 0x2b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013992] SRAT: PXM 0 -> APIC 0x2c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013993] SRAT: PXM 0 -> APIC 0x2d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013994] SRAT: PXM 0 -> APIC 0x2e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013995] SRAT: PXM 0 -> APIC 0x2f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013997] SRAT: PXM 0 -> APIC 0x30 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013998] SRAT: PXM 0 -> APIC 0x31 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.013999] SRAT: PXM 0 -> APIC 0x32 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014001] SRAT: PXM 0 -> APIC 0x33 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014002] SRAT: PXM 0 -> APIC 0x34 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014003] SRAT: PXM 0 -> APIC 0x35 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014005] SRAT: PXM 0 -> APIC 0x36 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014006] SRAT: PXM 0 -> APIC 0x37 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014007] SRAT: PXM 0 -> APIC 0x38 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014008] SRAT: PXM 0 -> APIC 0x39 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014010] SRAT: PXM 0 -> APIC 0x3a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014011] SRAT: PXM 0 -> APIC 0x3b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014012] SRAT: PXM 0 -> APIC 0x3c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014014] SRAT: PXM 0 -> APIC 0x3d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014015] SRAT: PXM 0 -> APIC 0x3e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014016] SRAT: PXM 0 -> APIC 0x3f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014018] SRAT: PXM 0 -> APIC 0x40 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014019] SRAT: PXM 0 -> APIC 0x41 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014020] SRAT: PXM 0 -> APIC 0x42 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014021] SRAT: PXM 0 -> APIC 0x43 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014023] SRAT: PXM 0 -> APIC 0x44 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014024] SRAT: PXM 0 -> APIC 0x45 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014025] SRAT: PXM 0 -> APIC 0x46 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014027] SRAT: PXM 0 -> APIC 0x47 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014028] SRAT: PXM 0 -> APIC 0x48 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014029] SRAT: PXM 0 -> APIC 0x49 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014031] SRAT: PXM 0 -> APIC 0x4a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014032] SRAT: PXM 0 -> APIC 0x4b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014033] SRAT: PXM 0 -> APIC 0x4c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014034] SRAT: PXM 0 -> APIC 0x4d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014036] SRAT: PXM 0 -> APIC 0x4e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014037] SRAT: PXM 0 -> APIC 0x4f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014038] SRAT: PXM 0 -> APIC 0x50 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014040] SRAT: PXM 0 -> APIC 0x51 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014041] SRAT: PXM 0 -> APIC 0x52 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014042] SRAT: PXM 0 -> APIC 0x53 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014044] SRAT: PXM 0 -> APIC 0x54 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014045] SRAT: PXM 0 -> APIC 0x55 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014046] SRAT: PXM 0 -> APIC 0x56 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014047] SRAT: PXM 0 -> APIC 0x57 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014049] SRAT: PXM 0 -> APIC 0x58 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014050] SRAT: PXM 0 -> APIC 0x59 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014051] SRAT: PXM 0 -> APIC 0x5a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014053] SRAT: PXM 0 -> APIC 0x5b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014054] SRAT: PXM 0 -> APIC 0x5c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014055] SRAT: PXM 0 -> APIC 0x5d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014057] SRAT: PXM 0 -> APIC 0x5e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014058] SRAT: PXM 0 -> APIC 0x5f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014059] SRAT: PXM 0 -> APIC 0x60 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014060] SRAT: PXM 0 -> APIC 0x61 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014062] SRAT: PXM 0 -> APIC 0x62 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014063] SRAT: PXM 0 -> APIC 0x63 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014064] SRAT: PXM 0 -> APIC 0x64 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014066] SRAT: PXM 0 -> APIC 0x65 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014067] SRAT: PXM 0 -> APIC 0x66 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014068] SRAT: PXM 0 -> APIC 0x67 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014070] SRAT: PXM 0 -> APIC 0x68 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014071] SRAT: PXM 0 -> APIC 0x69 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014072] SRAT: PXM 0 -> APIC 0x6a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014073] SRAT: PXM 0 -> APIC 0x6b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014075] SRAT: PXM 0 -> APIC 0x6c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014076] SRAT: PXM 0 -> APIC 0x6d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014077] SRAT: PXM 0 -> APIC 0x6e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014079] SRAT: PXM 0 -> APIC 0x6f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014080] SRAT: PXM 0 -> APIC 0x70 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014081] SRAT: PXM 0 -> APIC 0x71 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014083] SRAT: PXM 0 -> APIC 0x72 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014084] SRAT: PXM 0 -> APIC 0x73 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014085] SRAT: PXM 0 -> APIC 0x74 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014086] SRAT: PXM 0 -> APIC 0x75 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014088] SRAT: PXM 0 -> APIC 0x76 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014089] SRAT: PXM 0 -> APIC 0x77 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014090] SRAT: PXM 0 -> APIC 0x78 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014092] SRAT: PXM 0 -> APIC 0x79 -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014093] SRAT: PXM 0 -> APIC 0x7a -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014094] SRAT: PXM 0 -> APIC 0x7b -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014096] SRAT: PXM 0 -> APIC 0x7c -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014097] SRAT: PXM 0 -> APIC 0x7d -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014098] SRAT: PXM 0 -> APIC 0x7e -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014100] SRAT: PXM 0 -> APIC 0x7f -> Node 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014104] ACPI: SRAT: Node 0 PXM 0 [mem 0x00000000-0x0009ffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014108] ACPI: SRAT: Node 0 PXM 0 [mem 0x00100000-0xbfffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014110] ACPI: SRAT: Node 0 PXM 0 [mem 0x100000000-0x13fffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014113] ACPI: SRAT: Node 0 PXM 0 [mem 0x140000000-0x103fffffff] hotplug
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014120] NUMA: Node 0 [mem 0x00000000-0x0009ffff] + [mem 0x00100000-0xbfffffff] -> [mem 0x00000000-0xbfffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014124] NUMA: Node 0 [mem 0x00000000-0xbfffffff] + [mem 0x100000000-0x13fffffff] -> [mem 0x00000000-0x13fffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014141] NODE_DATA(0) allocated [mem 0x13ffd3000-0x13fffdfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014720] Zone ranges:
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014726]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014731]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014734]   Normal   [mem 0x0000000100000000-0x000000013fffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014737]   Device   empty
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014739] Movable zone start for each node
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014742] Early memory node ranges
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014743]   node   0: [mem 0x0000000000001000-0x000000000009dfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014746]   node   0: [mem 0x0000000000100000-0x00000000bfecffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014748]   node   0: [mem 0x00000000bff00000-0x00000000bfffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014750]   node   0: [mem 0x0000000100000000-0x000000013fffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014753] Initmem setup node 0 [mem 0x0000000000001000-0x000000013fffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014771] On node 0, zone DMA: 1 pages in unavailable ranges
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.014947] On node 0, zone DMA: 98 pages in unavailable ranges
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.053336] On node 0, zone DMA32: 48 pages in unavailable ranges
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.072982] ACPI: PM-Timer IO Port: 0x1008
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073004] system APIC only can use physical flat
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073029] ACPI: LAPIC_NMI (acpi_id[0x00] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073033] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073036] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073037] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073039] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073040] ACPI: LAPIC_NMI (acpi_id[0x05] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073041] ACPI: LAPIC_NMI (acpi_id[0x06] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073043] ACPI: LAPIC_NMI (acpi_id[0x07] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073044] ACPI: LAPIC_NMI (acpi_id[0x08] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073046] ACPI: LAPIC_NMI (acpi_id[0x09] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073047] ACPI: LAPIC_NMI (acpi_id[0x0a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073049] ACPI: LAPIC_NMI (acpi_id[0x0b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073050] ACPI: LAPIC_NMI (acpi_id[0x0c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073051] ACPI: LAPIC_NMI (acpi_id[0x0d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073053] ACPI: LAPIC_NMI (acpi_id[0x0e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073054] ACPI: LAPIC_NMI (acpi_id[0x0f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073056] ACPI: LAPIC_NMI (acpi_id[0x10] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073057] ACPI: LAPIC_NMI (acpi_id[0x11] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073059] ACPI: LAPIC_NMI (acpi_id[0x12] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073060] ACPI: LAPIC_NMI (acpi_id[0x13] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073062] ACPI: LAPIC_NMI (acpi_id[0x14] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073063] ACPI: LAPIC_NMI (acpi_id[0x15] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073065] ACPI: LAPIC_NMI (acpi_id[0x16] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073066] ACPI: LAPIC_NMI (acpi_id[0x17] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073067] ACPI: LAPIC_NMI (acpi_id[0x18] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073069] ACPI: LAPIC_NMI (acpi_id[0x19] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073070] ACPI: LAPIC_NMI (acpi_id[0x1a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073072] ACPI: LAPIC_NMI (acpi_id[0x1b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073073] ACPI: LAPIC_NMI (acpi_id[0x1c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073075] ACPI: LAPIC_NMI (acpi_id[0x1d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073076] ACPI: LAPIC_NMI (acpi_id[0x1e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073077] ACPI: LAPIC_NMI (acpi_id[0x1f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073079] ACPI: LAPIC_NMI (acpi_id[0x20] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073080] ACPI: LAPIC_NMI (acpi_id[0x21] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073082] ACPI: LAPIC_NMI (acpi_id[0x22] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073083] ACPI: LAPIC_NMI (acpi_id[0x23] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073085] ACPI: LAPIC_NMI (acpi_id[0x24] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073086] ACPI: LAPIC_NMI (acpi_id[0x25] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073087] ACPI: LAPIC_NMI (acpi_id[0x26] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073089] ACPI: LAPIC_NMI (acpi_id[0x27] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073090] ACPI: LAPIC_NMI (acpi_id[0x28] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073092] ACPI: LAPIC_NMI (acpi_id[0x29] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073093] ACPI: LAPIC_NMI (acpi_id[0x2a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073095] ACPI: LAPIC_NMI (acpi_id[0x2b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073096] ACPI: LAPIC_NMI (acpi_id[0x2c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073097] ACPI: LAPIC_NMI (acpi_id[0x2d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073099] ACPI: LAPIC_NMI (acpi_id[0x2e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073100] ACPI: LAPIC_NMI (acpi_id[0x2f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073102] ACPI: LAPIC_NMI (acpi_id[0x30] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073103] ACPI: LAPIC_NMI (acpi_id[0x31] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073105] ACPI: LAPIC_NMI (acpi_id[0x32] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073106] ACPI: LAPIC_NMI (acpi_id[0x33] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073107] ACPI: LAPIC_NMI (acpi_id[0x34] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073109] ACPI: LAPIC_NMI (acpi_id[0x35] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073110] ACPI: LAPIC_NMI (acpi_id[0x36] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073112] ACPI: LAPIC_NMI (acpi_id[0x37] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073113] ACPI: LAPIC_NMI (acpi_id[0x38] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073115] ACPI: LAPIC_NMI (acpi_id[0x39] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073116] ACPI: LAPIC_NMI (acpi_id[0x3a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073117] ACPI: LAPIC_NMI (acpi_id[0x3b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073119] ACPI: LAPIC_NMI (acpi_id[0x3c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073120] ACPI: LAPIC_NMI (acpi_id[0x3d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073122] ACPI: LAPIC_NMI (acpi_id[0x3e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073123] ACPI: LAPIC_NMI (acpi_id[0x3f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073125] ACPI: LAPIC_NMI (acpi_id[0x40] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073126] ACPI: LAPIC_NMI (acpi_id[0x41] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073127] ACPI: LAPIC_NMI (acpi_id[0x42] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073129] ACPI: LAPIC_NMI (acpi_id[0x43] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073130] ACPI: LAPIC_NMI (acpi_id[0x44] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073132] ACPI: LAPIC_NMI (acpi_id[0x45] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073133] ACPI: LAPIC_NMI (acpi_id[0x46] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073135] ACPI: LAPIC_NMI (acpi_id[0x47] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073136] ACPI: LAPIC_NMI (acpi_id[0x48] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073137] ACPI: LAPIC_NMI (acpi_id[0x49] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073139] ACPI: LAPIC_NMI (acpi_id[0x4a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073140] ACPI: LAPIC_NMI (acpi_id[0x4b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073142] ACPI: LAPIC_NMI (acpi_id[0x4c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073143] ACPI: LAPIC_NMI (acpi_id[0x4d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073145] ACPI: LAPIC_NMI (acpi_id[0x4e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073146] ACPI: LAPIC_NMI (acpi_id[0x4f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073147] ACPI: LAPIC_NMI (acpi_id[0x50] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073149] ACPI: LAPIC_NMI (acpi_id[0x51] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073150] ACPI: LAPIC_NMI (acpi_id[0x52] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073152] ACPI: LAPIC_NMI (acpi_id[0x53] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073153] ACPI: LAPIC_NMI (acpi_id[0x54] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073155] ACPI: LAPIC_NMI (acpi_id[0x55] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073156] ACPI: LAPIC_NMI (acpi_id[0x56] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073157] ACPI: LAPIC_NMI (acpi_id[0x57] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073159] ACPI: LAPIC_NMI (acpi_id[0x58] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073160] ACPI: LAPIC_NMI (acpi_id[0x59] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073162] ACPI: LAPIC_NMI (acpi_id[0x5a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073163] ACPI: LAPIC_NMI (acpi_id[0x5b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073165] ACPI: LAPIC_NMI (acpi_id[0x5c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073166] ACPI: LAPIC_NMI (acpi_id[0x5d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073167] ACPI: LAPIC_NMI (acpi_id[0x5e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073169] ACPI: LAPIC_NMI (acpi_id[0x5f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073170] ACPI: LAPIC_NMI (acpi_id[0x60] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073172] ACPI: LAPIC_NMI (acpi_id[0x61] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073173] ACPI: LAPIC_NMI (acpi_id[0x62] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073175] ACPI: LAPIC_NMI (acpi_id[0x63] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073176] ACPI: LAPIC_NMI (acpi_id[0x64] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073177] ACPI: LAPIC_NMI (acpi_id[0x65] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073179] ACPI: LAPIC_NMI (acpi_id[0x66] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073180] ACPI: LAPIC_NMI (acpi_id[0x67] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073182] ACPI: LAPIC_NMI (acpi_id[0x68] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073183] ACPI: LAPIC_NMI (acpi_id[0x69] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073185] ACPI: LAPIC_NMI (acpi_id[0x6a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073186] ACPI: LAPIC_NMI (acpi_id[0x6b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073187] ACPI: LAPIC_NMI (acpi_id[0x6c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073189] ACPI: LAPIC_NMI (acpi_id[0x6d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073190] ACPI: LAPIC_NMI (acpi_id[0x6e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073192] ACPI: LAPIC_NMI (acpi_id[0x6f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073193] ACPI: LAPIC_NMI (acpi_id[0x70] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073195] ACPI: LAPIC_NMI (acpi_id[0x71] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073196] ACPI: LAPIC_NMI (acpi_id[0x72] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073197] ACPI: LAPIC_NMI (acpi_id[0x73] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073199] ACPI: LAPIC_NMI (acpi_id[0x74] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073200] ACPI: LAPIC_NMI (acpi_id[0x75] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073202] ACPI: LAPIC_NMI (acpi_id[0x76] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073203] ACPI: LAPIC_NMI (acpi_id[0x77] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073205] ACPI: LAPIC_NMI (acpi_id[0x78] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073206] ACPI: LAPIC_NMI (acpi_id[0x79] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073208] ACPI: LAPIC_NMI (acpi_id[0x7a] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073209] ACPI: LAPIC_NMI (acpi_id[0x7b] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073210] ACPI: LAPIC_NMI (acpi_id[0x7c] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073212] ACPI: LAPIC_NMI (acpi_id[0x7d] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073213] ACPI: LAPIC_NMI (acpi_id[0x7e] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073215] ACPI: LAPIC_NMI (acpi_id[0x7f] high edge lint[0x1])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073314] IOAPIC[0]: apic_id 128, version 32, address 0xfec00000, GSI 0-23
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073325] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 high edge)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073339] ACPI: Using ACPI (MADT) for SMP configuration information
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073341] ACPI: HPET id: 0x8086af01 base: 0xfed00000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073349] TSC deadline timer available
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073351] smpboot: Allowing 128 CPUs, 124 hotplug CPUs
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073374] PM: hibernation: Registered nosave memory: [mem 0x00000000-0x00000fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073377] PM: hibernation: Registered nosave memory: [mem 0x0009e000-0x0009efff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073379] PM: hibernation: Registered nosave memory: [mem 0x0009f000-0x0009ffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073381] PM: hibernation: Registered nosave memory: [mem 0x000a0000-0x000dbfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073382] PM: hibernation: Registered nosave memory: [mem 0x000dc000-0x000fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073385] PM: hibernation: Registered nosave memory: [mem 0xbfed0000-0xbfefefff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073386] PM: hibernation: Registered nosave memory: [mem 0xbfeff000-0xbfefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073394] PM: hibernation: Registered nosave memory: [mem 0xc0000000-0xefffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073396] PM: hibernation: Registered nosave memory: [mem 0xf0000000-0xf7ffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073397] PM: hibernation: Registered nosave memory: [mem 0xf8000000-0xfebfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073398] PM: hibernation: Registered nosave memory: [mem 0xfec00000-0xfec0ffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073400] PM: hibernation: Registered nosave memory: [mem 0xfec10000-0xfedfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073401] PM: hibernation: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073402] PM: hibernation: Registered nosave memory: [mem 0xfee01000-0xfffdffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073403] PM: hibernation: Registered nosave memory: [mem 0xfffe0000-0xffffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073406] [mem 0xc0000000-0xefffffff] available for PCI devices
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073409] Booting paravirtualized kernel on VMware hypervisor
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073413] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.073427] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:128 nr_cpu_ids:128 nr_node_ids:1
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100488] percpu: Embedded 63 pages/cpu s221184 r8192 d28672 u262144
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100513] pcpu-alloc: s221184 r8192 d28672 u262144 alloc=1*2097152
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100519] pcpu-alloc: [0] 000 001 002 003 004 005 006 007 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100530] pcpu-alloc: [0] 008 009 010 011 012 013 014 015 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100540] pcpu-alloc: [0] 016 017 018 019 020 021 022 023 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100549] pcpu-alloc: [0] 024 025 026 027 028 029 030 031 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100558] pcpu-alloc: [0] 032 033 034 035 036 037 038 039 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100568] pcpu-alloc: [0] 040 041 042 043 044 045 046 047 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100577] pcpu-alloc: [0] 048 049 050 051 052 053 054 055 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100586] pcpu-alloc: [0] 056 057 058 059 060 061 062 063 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100595] pcpu-alloc: [0] 064 065 066 067 068 069 070 071 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100604] pcpu-alloc: [0] 072 073 074 075 076 077 078 079 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100613] pcpu-alloc: [0] 080 081 082 083 084 085 086 087 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100622] pcpu-alloc: [0] 088 089 090 091 092 093 094 095 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100631] pcpu-alloc: [0] 096 097 098 099 100 101 102 103 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100640] pcpu-alloc: [0] 104 105 106 107 108 109 110 111 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100649] pcpu-alloc: [0] 112 113 114 115 116 117 118 119 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100659] pcpu-alloc: [0] 120 121 122 123 124 125 126 127 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100714] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic root=UUID=4a64a517-67dd-4c66-898a-7aec80564857 ro find_preseed=/preseed.cfg auto noprompt priority=critical locale=en_US quiet splash
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100938] Unknown kernel command line parameters "auto noprompt splash BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic find_preseed=/preseed.cfg priority=critical locale=en_US", will be passed to user space.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100983] random: crng init done
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100986] printk: log_buf_len individual max cpu contribution: 4096 bytes
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100988] printk: log_buf_len total cpu_extra contributions: 520192 bytes
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.100989] printk: log_buf_len min size: 262144 bytes
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.104657] printk: log_buf_len: 1048576 bytes
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.104660] printk: early log buf free: 237936(90%)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.111044] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.112411] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.117147] Fallback order for Node 0: 0 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.117175] Built 1 zonelists, mobility grouping on.  Total pages: 1031888
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.117179] Policy zone: Normal
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.117191] mem auto-init: stack:all(zero), heap alloc:on, heap free:off
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.117201] software IO TLB: area num 128.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.173763] Memory: 3886596K/4193716K available (20480K kernel code, 4264K rwdata, 13180K rodata, 4792K init, 17396K bss, 306860K reserved, 0K cma-reserved)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.174484] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=128, Nodes=1
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.174604] ftrace: allocating 55206 entries in 216 pages
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.184681] ftrace: allocated 216 pages with 4 groups
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186073] Dynamic Preempt: voluntary
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186482] rcu: Preemptible hierarchical RCU implementation.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186484] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=128.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186487] 	Trampoline variant of Tasks RCU enabled.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186488] 	Rude variant of Tasks RCU enabled.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186489] 	Tracing variant of Tasks RCU enabled.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186490] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.186492] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=128
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.193287] NR_IRQS: 524544, nr_irqs: 1448, preallocated irqs: 16
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.193746] rcu: srcu_init: Setting srcu_struct sizes to big.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.199335] Console: colour VGA+ 80x25
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.199341] printk: console [tty0] enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.199633] ACPI: Core revision 20230331
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.200818] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.200987] APIC: Switch to symmetric I/O mode setup
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.202348] x2apic enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.203017] Switched APIC routing to physical x2apic.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.205948] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206032] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x22df12c5959, max_idle_ns: 440795242016 ns
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206045] Calibrating delay loop (skipped) preset value.. 4838.40 BogoMIPS (lpj=9676808)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206268] x86/cpu: User Mode Instruction Prevention (UMIP) activated
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206432] Last level iTLB entries: 4KB 0, 2MB 0, 4MB 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206436] Last level dTLB entries: 4KB 0, 2MB 0, 4MB 0, 1GB 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206444] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206449] Spectre V2 : Mitigation: Enhanced / Automatic IBRS
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206450] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206452] Spectre V2 : Spectre v2 / PBRSB-eIBRS: Retire a single CALL on VMEXIT
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206456] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206459] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206461] MMIO Stale Data: Unknown: No mitigations
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206493] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206496] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206498] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206499] x86/fpu: Supporting XSAVE feature 0x200: 'Protection Keys User registers'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206502] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206505] x86/fpu: xstate_offset[9]:  832, xstate_sizes[9]:    8
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.206507] x86/fpu: Enabled xstate features 0x207, context size is 840 bytes, using 'compacted' format.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.246431] Freeing SMP alternatives memory: 44K
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.246449] pid_max: default: 131072 minimum: 1024
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.246630] LSM: initializing lsm=lockdown,capability,landlock,yama,apparmor,integrity
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.246680] landlock: Up and running.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.246682] Yama: becoming mindful.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.246777] AppArmor: AppArmor initialized
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.246978] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.247036] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] smpboot: CPU0: Intel(R) Core(TM) i7-14650HX (family: 0x6, model: 0xb7, stepping: 0x1)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] RCU Tasks: Setting shift to 7 and lim to 1 rcu_task_cb_adjust=1.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] RCU Tasks Rude: Setting shift to 7 and lim to 1 rcu_task_cb_adjust=1.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] RCU Tasks Trace: Setting shift to 7 and lim to 1 rcu_task_cb_adjust=1.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] Performance Events: Alderlake Hybrid events, core PMU driver.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: CPUID marked event: 'cpu cycles' unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: CPUID marked event: 'instructions' unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: CPUID marked event: 'bus cycles' unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: CPUID marked event: 'cache references' unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: CPUID marked event: 'cache misses' unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: CPUID marked event: 'branch instructions' unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: CPUID marked event: 'branch misses' unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] core: cpu_core PMU driver: 
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] ... version:                1
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] ... bit width:              48
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] ... generic registers:      6
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] ... value mask:             0000ffffffffffff
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] ... max period:             000000007fffffff
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] ... fixed-purpose events:   0
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] ... event mask:             0001000f0000003f
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] signal: max sigframe size: 3632
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] rcu: Hierarchical SRCU implementation.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] rcu: 	Max phase no-delay instances is 1000.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.262039] NMI watchdog: Perf NMI watchdog permanently disabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.266039] smp: Bringing up secondary CPUs ...
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.266039] smpboot: x86: Booting SMP configuration:
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.266039] .... node  #0, CPUs:          #1   #2   #3
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.015918] smpboot: CPU 2 Converting physical 0 to logical die 1
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.285640] smp: Brought up 1 node, 4 CPUs
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.285652] smpboot: Max logical packages: 64
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.285657] smpboot: Total of 4 processors activated (19353.61 BogoMIPS)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.290290] devtmpfs: initialized
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.290290] x86/mm: Memory block size: 128MB
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.291559] ACPI: PM: Registering ACPI NVS region [mem 0xbfeff000-0xbfefffff] (4096 bytes)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.291559] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.292315] futex hash table entries: 32768 (order: 9, 2097152 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.294129] pinctrl core: initialized pinctrl subsystem
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.294514] PM: RTC time: 09:29:16, date: 2026-06-30
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298039] NET: Registered PF_NETLINK/PF_ROUTE protocol family
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298174] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298670] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298747] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298781] audit: initializing netlink subsys (disabled)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] thermal_sys: Registered thermal governor 'fair_share'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] thermal_sys: Registered thermal governor 'bang_bang'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] thermal_sys: Registered thermal governor 'step_wise'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] thermal_sys: Registered thermal governor 'user_space'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] thermal_sys: Registered thermal governor 'power_allocator'
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] EISA bus registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] audit: type=2000 audit(1782811756.092:1): state=initialized audit_enabled=0 res=1
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.298824] cpuidle: using governor ladder
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.299234] cpuidle: using governor menu
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.299374] Simple Boot Flag at 0x36 set to 0x80
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.299443] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.302282] PCI: MMCONFIG for domain 0000 [bus 00-7f] at [mem 0xf0000000-0xf7ffffff] (base 0xf0000000)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.302292] PCI: MMCONFIG at [mem 0xf0000000-0xf7ffffff] reserved as E820 entry
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.302311] PCI: Using configuration type 1 for base access
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.306039] kprobes: kprobe jump-optimization is enabled. All kprobes are optimized if possible.
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.306235] HugeTLB: registered 1.00 GiB page size, pre-allocated 0 pages
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.306235] HugeTLB: 16380 KiB vmemmap can be freed for a 1.00 GiB page
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.306235] HugeTLB: registered 2.00 MiB page size, pre-allocated 0 pages
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.306235] HugeTLB: 28 KiB vmemmap can be freed for a 2.00 MiB page
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.310736] ACPI: Added _OSI(Module Device)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.310740] ACPI: Added _OSI(Processor Device)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.310742] ACPI: Added _OSI(3.0 _SCP Extensions)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.310744] ACPI: Added _OSI(Processor Aggregator Device)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.349830] ACPI: 1 ACPI AML tables successfully acquired and loaded
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.354614] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.398039] ACPI: Interpreter enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.398039] ACPI: PM: (supports S0 S1 S4 S5)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.398039] ACPI: Using IOAPIC for interrupt routing
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.405255] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.405260] PCI: Using E820 reservations for host bridge windows
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.408506] ACPI: Enabled 4 GPEs in block 00 to 0F
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.741493] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-7f])
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.741515] acpi PNP0A03:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI EDR HPX-Type3]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.741740] acpi PNP0A03:00: _OSC: platform does not support [AER LTR DPC]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.742161] acpi PNP0A03:00: _OSC: OS now controls [PCIeHotplug SHPCHotplug PME PCIeCapability]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748298] PCI host bridge to bus 0000:00
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748312] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748320] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000dbfff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748323] pci_bus 0000:00: root bus resource [mem 0xc0000000-0xfebfffff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748326] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748329] pci_bus 0000:00: root bus resource [io  0x0d00-0xfeff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748332] pci_bus 0000:00: root bus resource [bus 00-7f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748636] pci 0000:00:00.0: [8086:7190] type 00 class 0x060000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.748636] pci 0000:00:01.0: [8086:7191] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.750039] pci 0000:00:07.0: [8086:7110] type 00 class 0x060100
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.750039] pci 0000:00:07.1: [8086:7111] type 00 class 0x01018a
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.758052] pci 0000:00:07.1: reg 0x20: [io  0x1060-0x106f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.759369] pci 0000:00:07.1: legacy IDE quirk: reg 0x10: [io  0x01f0-0x01f7]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.759377] pci 0000:00:07.1: legacy IDE quirk: reg 0x14: [io  0x03f6]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.759380] pci 0000:00:07.1: legacy IDE quirk: reg 0x18: [io  0x0170-0x0177]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.759383] pci 0000:00:07.1: legacy IDE quirk: reg 0x1c: [io  0x0376]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.759951] pci 0000:00:07.3: [8086:7113] type 00 class 0x068000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.765617] pci 0000:00:07.3: quirk: [io  0x1000-0x103f] claimed by PIIX4 ACPI
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.765648] pci 0000:00:07.3: quirk: [io  0x1040-0x104f] claimed by PIIX4 SMB
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.765648] pci 0000:00:07.7: [15ad:0740] type 00 class 0x088000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.766043] pci 0000:00:07.7: reg 0x10: [io  0x1080-0x10bf]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.766774] pci 0000:00:07.7: reg 0x14: [mem 0xfebc0000-0xfebfffff 64bit]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.769686] pci 0000:00:0f.0: [15ad:0405] type 00 class 0x030000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.770039] pci 0000:00:0f.0: reg 0x10: [io  0x1070-0x107f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.770039] pci 0000:00:0f.0: reg 0x14: [mem 0xe8000000-0xefffffff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.770039] pci 0000:00:0f.0: reg 0x18: [mem 0xfe000000-0xfe7fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.779732] pci 0000:00:0f.0: reg 0x30: [mem 0x00000000-0x00007fff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.779775] pci 0000:00:0f.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.780089] pci 0000:00:10.0: [1000:0030] type 00 class 0x010000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.780570] pci 0000:00:10.0: reg 0x10: [io  0x1400-0x14ff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.781085] pci 0000:00:10.0: reg 0x14: [mem 0xfeb80000-0xfeb9ffff 64bit]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.781629] pci 0000:00:10.0: reg 0x1c: [mem 0xfeba0000-0xfebbffff 64bit]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.781629] pci 0000:00:10.0: reg 0x30: [mem 0x00000000-0x00003fff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.781629] pci 0000:00:11.0: [15ad:0790] type 01 class 0x060401
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.781629] pci 0000:00:15.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.781629] pci 0000:00:15.0: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.782039] pci 0000:00:15.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.786850] pci 0000:00:15.1: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.788001] pci 0000:00:15.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.789838] pci 0000:00:15.2: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.790959] pci 0000:00:15.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.792792] pci 0000:00:15.3: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.794158] pci 0000:00:15.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.796027] pci 0000:00:15.4: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.797111] pci 0000:00:15.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.798966] pci 0000:00:15.5: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.800040] pci 0000:00:15.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.802547] pci 0000:00:15.6: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.803713] pci 0000:00:15.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.805691] pci 0000:00:15.7: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.807159] pci 0000:00:16.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.809353] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.810506] pci 0000:00:16.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.813191] pci 0000:00:16.1: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.813191] pci 0000:00:16.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.813191] pci 0000:00:16.2: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.813468] pci 0000:00:16.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.814039] pci 0000:00:16.3: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.814039] pci 0000:00:16.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.818353] pci 0000:00:16.4: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.819452] pci 0000:00:16.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.821472] pci 0000:00:16.5: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.822092] pci 0000:00:16.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.823952] pci 0000:00:16.6: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.825097] pci 0000:00:16.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.826941] pci 0000:00:16.7: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.828037] pci 0000:00:17.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.829901] pci 0000:00:17.0: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.830987] pci 0000:00:17.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.832849] pci 0000:00:17.1: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.833923] pci 0000:00:17.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.835850] pci 0000:00:17.2: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.837056] pci 0000:00:17.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.838924] pci 0000:00:17.3: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.840061] pci 0000:00:17.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.841909] pci 0000:00:17.4: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.842977] pci 0000:00:17.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.844813] pci 0000:00:17.5: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.846068] pci 0000:00:17.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.847908] pci 0000:00:17.6: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.849035] pci 0000:00:17.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.850894] pci 0000:00:17.7: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.851927] pci 0000:00:18.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.853753] pci 0000:00:18.0: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.855909] pci 0000:00:18.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.857785] pci 0000:00:18.1: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.858875] pci 0000:00:18.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.860724] pci 0000:00:18.2: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.861827] pci 0000:00:18.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.863652] pci 0000:00:18.3: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.864736] pci 0000:00:18.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.866575] pci 0000:00:18.4: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.867805] pci 0000:00:18.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.869813] pci 0000:00:18.5: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.871020] pci 0000:00:18.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.873313] pci 0000:00:18.6: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.874659] pci 0000:00:18.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.876657] pci 0000:00:18.7: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.878194] pci_bus 0000:01: extended config space not accessible
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.898912] pci 0000:00:01.0: PCI bridge to [bus 01]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.899408] pci_bus 0000:02: extended config space not accessible
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.899856] acpiphp: Slot [32] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.899903] acpiphp: Slot [33] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.899946] acpiphp: Slot [34] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.899987] acpiphp: Slot [35] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.900028] acpiphp: Slot [36] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.900071] acpiphp: Slot [37] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.900111] acpiphp: Slot [38] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.900150] acpiphp: Slot [39] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.900199] acpiphp: Slot [40] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.900946] acpiphp: Slot [41] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901100] acpiphp: Slot [42] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901142] acpiphp: Slot [43] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901184] acpiphp: Slot [44] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901224] acpiphp: Slot [45] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901264] acpiphp: Slot [46] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901304] acpiphp: Slot [47] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901357] acpiphp: Slot [48] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901398] acpiphp: Slot [49] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901438] acpiphp: Slot [50] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901478] acpiphp: Slot [51] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901520] acpiphp: Slot [52] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901560] acpiphp: Slot [53] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901600] acpiphp: Slot [54] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901640] acpiphp: Slot [55] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901688] acpiphp: Slot [56] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901729] acpiphp: Slot [57] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901769] acpiphp: Slot [58] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901809] acpiphp: Slot [59] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901849] acpiphp: Slot [60] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901889] acpiphp: Slot [61] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901929] acpiphp: Slot [62] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.901969] acpiphp: Slot [63] registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.902196] pci 0000:02:00.0: [15ad:0774] type 00 class 0x0c0300
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.907214] pci 0000:02:00.0: reg 0x20: [io  0x2080-0x209f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.907214] pci 0000:02:01.0: [8086:100f] type 00 class 0x020000
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.910039] pci 0000:02:01.0: reg 0x10: [mem 0xfd5c0000-0xfd5dffff 64bit]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.914047] pci 0000:02:01.0: reg 0x18: [mem 0xfdff0000-0xfdffffff 64bit]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.914788] pci 0000:02:01.0: reg 0x20: [io  0x2000-0x203f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.916528] pci 0000:02:01.0: reg 0x30: [mem 0x00000000-0x0000ffff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.916926] pci 0000:02:01.0: PME# supported from D0 D3hot D3cold
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.917623] pci 0000:02:02.0: [1274:1371] type 00 class 0x040100
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.918043] pci 0000:02:02.0: reg 0x10: [io  0x2040-0x207f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.925932] pci 0000:02:03.0: [15ad:0770] type 00 class 0x0c0320
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.927271] pci 0000:02:03.0: reg 0x10: [mem 0xfd5ef000-0xfd5effff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.930417] pci 0000:02:04.0: [15ad:07e0] type 00 class 0x010601
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.932245] pci 0000:02:04.0: reg 0x24: [mem 0xfd5ee000-0xfd5eefff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.932462] pci 0000:02:04.0: reg 0x30: [mem 0x00000000-0x0000ffff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.932732] pci 0000:02:04.0: PME# supported from D3hot
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948739] pci 0000:00:11.0: PCI bridge to [bus 02] (subtractive decode)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948798] pci 0000:00:11.0:   bridge window [io  0x2000-0x3fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948847] pci 0000:00:11.0:   bridge window [mem 0xfd500000-0xfdffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948937] pci 0000:00:11.0:   bridge window [mem 0xe7b00000-0xe7ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948942] pci 0000:00:11.0:   bridge window [mem 0x000a0000-0x000bffff window] (subtractive decode)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948946] pci 0000:00:11.0:   bridge window [mem 0x000d0000-0x000dbfff window] (subtractive decode)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948949] pci 0000:00:11.0:   bridge window [mem 0xc0000000-0xfebfffff window] (subtractive decode)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948952] pci 0000:00:11.0:   bridge window [io  0x0000-0x0cf7 window] (subtractive decode)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.948955] pci 0000:00:11.0:   bridge window [io  0x0d00-0xfeff window] (subtractive decode)
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.950192] pci 0000:00:15.0: PCI bridge to [bus 03]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.950243] pci 0000:00:15.0:   bridge window [io  0x4000-0x4fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.950290] pci 0000:00:15.0:   bridge window [mem 0xfd400000-0xfd4fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.950379] pci 0000:00:15.0:   bridge window [mem 0xe7a00000-0xe7afffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.951578] pci 0000:00:15.1: PCI bridge to [bus 04]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.951626] pci 0000:00:15.1:   bridge window [io  0x8000-0x8fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.951673] pci 0000:00:15.1:   bridge window [mem 0xfd000000-0xfd0fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.951761] pci 0000:00:15.1:   bridge window [mem 0xe7600000-0xe76fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.953095] pci 0000:00:15.2: PCI bridge to [bus 05]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.953160] pci 0000:00:15.2:   bridge window [io  0xc000-0xcfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.953214] pci 0000:00:15.2:   bridge window [mem 0xfcc00000-0xfccfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.953305] pci 0000:00:15.2:   bridge window [mem 0xe7200000-0xe72fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.954512] pci 0000:00:15.3: PCI bridge to [bus 06]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.954605] pci 0000:00:15.3:   bridge window [mem 0xfc800000-0xfc8fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.954706] pci 0000:00:15.3:   bridge window [mem 0xe6e00000-0xe6efffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.955897] pci 0000:00:15.4: PCI bridge to [bus 07]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.955987] pci 0000:00:15.4:   bridge window [mem 0xfc400000-0xfc4fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.956076] pci 0000:00:15.4:   bridge window [mem 0xe6a00000-0xe6afffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.957291] pci 0000:00:15.5: PCI bridge to [bus 08]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.957381] pci 0000:00:15.5:   bridge window [mem 0xfc000000-0xfc0fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.957589] pci 0000:00:15.5:   bridge window [mem 0xe6600000-0xe66fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.958789] pci 0000:00:15.6: PCI bridge to [bus 09]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.958881] pci 0000:00:15.6:   bridge window [mem 0xfbc00000-0xfbcfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.958970] pci 0000:00:15.6:   bridge window [mem 0xe6200000-0xe62fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.960157] pci 0000:00:15.7: PCI bridge to [bus 0a]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.960248] pci 0000:00:15.7:   bridge window [mem 0xfb800000-0xfb8fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.960336] pci 0000:00:15.7:   bridge window [mem 0xe5e00000-0xe5efffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.961728] pci 0000:00:16.0: PCI bridge to [bus 0b]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.961779] pci 0000:00:16.0:   bridge window [io  0x5000-0x5fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.961826] pci 0000:00:16.0:   bridge window [mem 0xfd300000-0xfd3fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.961917] pci 0000:00:16.0:   bridge window [mem 0xe7900000-0xe79fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.963065] pci 0000:00:16.1: PCI bridge to [bus 0c]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.963114] pci 0000:00:16.1:   bridge window [io  0x9000-0x9fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.963160] pci 0000:00:16.1:   bridge window [mem 0xfcf00000-0xfcffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.963248] pci 0000:00:16.1:   bridge window [mem 0xe7500000-0xe75fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.964422] pci 0000:00:16.2: PCI bridge to [bus 0d]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.964470] pci 0000:00:16.2:   bridge window [io  0xd000-0xdfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.964516] pci 0000:00:16.2:   bridge window [mem 0xfcb00000-0xfcbfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.964605] pci 0000:00:16.2:   bridge window [mem 0xe7100000-0xe71fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965781] pci 0000:00:16.3: PCI bridge to [bus 0e]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965871] pci 0000:00:16.3:   bridge window [mem 0xfc700000-0xfc7fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965960] pci 0000:00:16.3:   bridge window [mem 0xe6d00000-0xe6dfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965960] pci 0000:00:16.4: PCI bridge to [bus 0f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965960] pci 0000:00:16.4:   bridge window [mem 0xfc300000-0xfc3fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965960] pci 0000:00:16.4:   bridge window [mem 0xe6900000-0xe69fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965960] pci 0000:00:16.5: PCI bridge to [bus 10]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965960] pci 0000:00:16.5:   bridge window [mem 0xfbf00000-0xfbffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965960] pci 0000:00:16.5:   bridge window [mem 0xe6500000-0xe65fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.965974] pci 0000:00:16.6: PCI bridge to [bus 11]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:16.6:   bridge window [mem 0xfbb00000-0xfbbfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:16.6:   bridge window [mem 0xe6100000-0xe61fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:16.7: PCI bridge to [bus 12]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:16.7:   bridge window [mem 0xfb700000-0xfb7fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:16.7:   bridge window [mem 0xe5d00000-0xe5dfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:17.0: PCI bridge to [bus 13]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:17.0:   bridge window [io  0x6000-0x6fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:17.0:   bridge window [mem 0xfd200000-0xfd2fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.966039] pci 0000:00:17.0:   bridge window [mem 0xe7800000-0xe78fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.974387] pci 0000:00:17.1: PCI bridge to [bus 14]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.974453] pci 0000:00:17.1:   bridge window [io  0xa000-0xafff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.974505] pci 0000:00:17.1:   bridge window [mem 0xfce00000-0xfcefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.974594] pci 0000:00:17.1:   bridge window [mem 0xe7400000-0xe74fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.975828] pci 0000:00:17.2: PCI bridge to [bus 15]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.975877] pci 0000:00:17.2:   bridge window [io  0xe000-0xefff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.975924] pci 0000:00:17.2:   bridge window [mem 0xfca00000-0xfcafffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.976012] pci 0000:00:17.2:   bridge window [mem 0xe7000000-0xe70fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.977262] pci 0000:00:17.3: PCI bridge to [bus 16]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.977355] pci 0000:00:17.3:   bridge window [mem 0xfc600000-0xfc6fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.977445] pci 0000:00:17.3:   bridge window [mem 0xe6c00000-0xe6cfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.978660] pci 0000:00:17.4: PCI bridge to [bus 17]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.978751] pci 0000:00:17.4:   bridge window [mem 0xfc200000-0xfc2fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.978840] pci 0000:00:17.4:   bridge window [mem 0xe6800000-0xe68fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.980009] pci 0000:00:17.5: PCI bridge to [bus 18]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.980098] pci 0000:00:17.5:   bridge window [mem 0xfbe00000-0xfbefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.980208] pci 0000:00:17.5:   bridge window [mem 0xe6400000-0xe64fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.981383] pci 0000:00:17.6: PCI bridge to [bus 19]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.981474] pci 0000:00:17.6:   bridge window [mem 0xfba00000-0xfbafffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.981562] pci 0000:00:17.6:   bridge window [mem 0xe6000000-0xe60fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.983268] pci 0000:00:17.7: PCI bridge to [bus 1a]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.983366] pci 0000:00:17.7:   bridge window [mem 0xfb600000-0xfb6fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.983455] pci 0000:00:17.7:   bridge window [mem 0xe5c00000-0xe5cfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.984710] pci 0000:00:18.0: PCI bridge to [bus 1b]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.984758] pci 0000:00:18.0:   bridge window [io  0x7000-0x7fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.984805] pci 0000:00:18.0:   bridge window [mem 0xfd100000-0xfd1fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.984893] pci 0000:00:18.0:   bridge window [mem 0xe7700000-0xe77fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.986039] pci 0000:00:18.1: PCI bridge to [bus 1c]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.986069] pci 0000:00:18.1:   bridge window [io  0xb000-0xbfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.986116] pci 0000:00:18.1:   bridge window [mem 0xfcd00000-0xfcdfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.986205] pci 0000:00:18.1:   bridge window [mem 0xe7300000-0xe73fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.987555] pci 0000:00:18.2: PCI bridge to [bus 1d]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.987647] pci 0000:00:18.2:   bridge window [mem 0xfc900000-0xfc9fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.987765] pci 0000:00:18.2:   bridge window [mem 0xe6f00000-0xe6ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.988941] pci 0000:00:18.3: PCI bridge to [bus 1e]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.989031] pci 0000:00:18.3:   bridge window [mem 0xfc500000-0xfc5fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.989120] pci 0000:00:18.3:   bridge window [mem 0xe6b00000-0xe6bfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.990039] pci 0000:00:18.4: PCI bridge to [bus 1f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.990112] pci 0000:00:18.4:   bridge window [mem 0xfc100000-0xfc1fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.990201] pci 0000:00:18.4:   bridge window [mem 0xe6700000-0xe67fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.991537] pci 0000:00:18.5: PCI bridge to [bus 20]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.991628] pci 0000:00:18.5:   bridge window [mem 0xfbd00000-0xfbdfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.991716] pci 0000:00:18.5:   bridge window [mem 0xe6300000-0xe63fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.992922] pci 0000:00:18.6: PCI bridge to [bus 21]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.993013] pci 0000:00:18.6:   bridge window [mem 0xfb900000-0xfb9fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.993101] pci 0000:00:18.6:   bridge window [mem 0xe5f00000-0xe5ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.994056] pci 0000:00:18.7: PCI bridge to [bus 22]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.994148] pci 0000:00:18.7:   bridge window [mem 0xfb500000-0xfb5fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    0.994237] pci 0000:00:18.7:   bridge window [mem 0xe5b00000-0xe5bfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.002153] ACPI: PCI: Interrupt link LNKA configured for IRQ 9
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.002349] ACPI: PCI: Interrupt link LNKB configured for IRQ 11
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.002534] ACPI: PCI: Interrupt link LNKC configured for IRQ 10
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.002717] ACPI: PCI: Interrupt link LNKD configured for IRQ 7
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078115] iommu: Default domain type: Translated
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078115] iommu: DMA domain TLB invalidation policy: lazy mode
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078551] SCSI subsystem initialized
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078799] libata version 3.00 loaded.
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078860] ACPI: bus type USB registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078881] usbcore: registered new interface driver usbfs
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078908] usbcore: registered new interface driver hub
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.078974] usbcore: registered new device driver usb
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.079051] pps_core: LinuxPPS API ver. 1 registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.079054] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.079059] PTP clock support registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.079143] EDAC MC: Ver: 3.0.0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.090370] NetLabel: Initializing
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.090376] NetLabel:  domain hash size = 128
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.090379] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.090415] NetLabel:  unlabeled traffic allowed by default
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.090488] mctp: management component transport protocol core
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.090488] NET: Registered PF_MCTP protocol family
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.090488] PCI: Using ACPI for IRQ routing
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.151829] PCI: pci_cache_line_size set to 64 bytes
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.153926] e820: reserve RAM buffer [mem 0x0009e800-0x0009ffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.153933] e820: reserve RAM buffer [mem 0xbfed0000-0xbfffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.154092] pci 0000:00:0f.0: vgaarb: setting as boot VGA device
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.154098] pci 0000:00:0f.0: vgaarb: bridge control possible
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.154100] pci 0000:00:0f.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.154120] vgaarb: loaded
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.154871] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.154871] hpet0: 16 comparators, 64-bit 14.318180 MHz counter
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.158048] clocksource: Switched to clocksource tsc-early
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.158833] VFS: Disk quotas dquot_6.6.0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.158913] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.159362] AppArmor: AppArmor Filesystem Enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.159399] pnp: PnP ACPI init
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.159809] system 00:00: [io  0x1000-0x103f] has been reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.159816] system 00:00: [io  0x1040-0x104f] has been reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.159820] system 00:00: [io  0x0cf0-0x0cf1] has been reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.160451] system 00:04: [mem 0xfed00000-0xfed003ff] has been reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.164643] pnp 00:06: [dma 2]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.165150] system 00:07: [io  0xfce0-0xfcff] has been reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.165157] system 00:07: [mem 0xf0000000-0xf7ffffff] has been reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.165161] system 00:07: [mem 0xfe800000-0xfe9fffff] has been reserved
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.227544] pnp: PnP ACPI: found 8 devices
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.267147] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.267384] NET: Registered PF_INET protocol family
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.268006] IP idents hash table entries: 65536 (order: 7, 524288 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.275242] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.275494] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.275729] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.276970] TCP bind hash table entries: 32768 (order: 8, 1048576 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.277120] TCP: Hash tables configured (established 32768 bind 32768)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.277984] MPTCP token hash table entries: 4096 (order: 4, 98304 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278096] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278196] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278722] NET: Registered PF_UNIX/PF_LOCAL protocol family
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278736] NET: Registered PF_XDP protocol family
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278767] pci 0000:00:15.3: bridge window [io  0x1000-0x0fff] to [bus 06] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278775] pci 0000:00:15.4: bridge window [io  0x1000-0x0fff] to [bus 07] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278779] pci 0000:00:15.5: bridge window [io  0x1000-0x0fff] to [bus 08] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278783] pci 0000:00:15.6: bridge window [io  0x1000-0x0fff] to [bus 09] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278786] pci 0000:00:15.7: bridge window [io  0x1000-0x0fff] to [bus 0a] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278791] pci 0000:00:16.3: bridge window [io  0x1000-0x0fff] to [bus 0e] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278795] pci 0000:00:16.4: bridge window [io  0x1000-0x0fff] to [bus 0f] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278799] pci 0000:00:16.5: bridge window [io  0x1000-0x0fff] to [bus 10] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278802] pci 0000:00:16.6: bridge window [io  0x1000-0x0fff] to [bus 11] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278807] pci 0000:00:16.7: bridge window [io  0x1000-0x0fff] to [bus 12] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278815] pci 0000:00:17.3: bridge window [io  0x1000-0x0fff] to [bus 16] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278818] pci 0000:00:17.4: bridge window [io  0x1000-0x0fff] to [bus 17] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278821] pci 0000:00:17.5: bridge window [io  0x1000-0x0fff] to [bus 18] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278824] pci 0000:00:17.6: bridge window [io  0x1000-0x0fff] to [bus 19] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278828] pci 0000:00:17.7: bridge window [io  0x1000-0x0fff] to [bus 1a] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278832] pci 0000:00:18.2: bridge window [io  0x1000-0x0fff] to [bus 1d] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278835] pci 0000:00:18.3: bridge window [io  0x1000-0x0fff] to [bus 1e] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278838] pci 0000:00:18.4: bridge window [io  0x1000-0x0fff] to [bus 1f] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278842] pci 0000:00:18.5: bridge window [io  0x1000-0x0fff] to [bus 20] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278845] pci 0000:00:18.6: bridge window [io  0x1000-0x0fff] to [bus 21] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278848] pci 0000:00:18.7: bridge window [io  0x1000-0x0fff] to [bus 22] add_size 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278884] pci 0000:00:10.0: BAR 6: assigned [mem 0xc0000000-0xc0003fff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278891] pci 0000:00:15.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278895] pci 0000:00:15.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278899] pci 0000:00:15.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278901] pci 0000:00:15.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278905] pci 0000:00:15.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278907] pci 0000:00:15.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278911] pci 0000:00:15.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278913] pci 0000:00:15.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278916] pci 0000:00:15.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278918] pci 0000:00:15.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278921] pci 0000:00:16.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278924] pci 0000:00:16.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278927] pci 0000:00:16.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278929] pci 0000:00:16.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278932] pci 0000:00:16.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278935] pci 0000:00:16.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278938] pci 0000:00:16.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278940] pci 0000:00:16.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278943] pci 0000:00:16.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278945] pci 0000:00:16.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278949] pci 0000:00:17.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278951] pci 0000:00:17.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278954] pci 0000:00:17.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278956] pci 0000:00:17.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278960] pci 0000:00:17.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278962] pci 0000:00:17.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278965] pci 0000:00:17.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278968] pci 0000:00:17.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278971] pci 0000:00:17.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278973] pci 0000:00:17.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278976] pci 0000:00:18.2: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278979] pci 0000:00:18.2: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278982] pci 0000:00:18.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278984] pci 0000:00:18.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278987] pci 0000:00:18.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278990] pci 0000:00:18.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278993] pci 0000:00:18.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278995] pci 0000:00:18.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.278998] pci 0000:00:18.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279001] pci 0000:00:18.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279004] pci 0000:00:18.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279006] pci 0000:00:18.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279014] pci 0000:00:18.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279017] pci 0000:00:18.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279020] pci 0000:00:18.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279022] pci 0000:00:18.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279026] pci 0000:00:18.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279028] pci 0000:00:18.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279031] pci 0000:00:18.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279033] pci 0000:00:18.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279037] pci 0000:00:18.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279039] pci 0000:00:18.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279042] pci 0000:00:18.2: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279045] pci 0000:00:18.2: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279048] pci 0000:00:17.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279050] pci 0000:00:17.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279053] pci 0000:00:17.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279056] pci 0000:00:17.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279059] pci 0000:00:17.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279061] pci 0000:00:17.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279065] pci 0000:00:17.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279067] pci 0000:00:17.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279070] pci 0000:00:17.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279072] pci 0000:00:17.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279076] pci 0000:00:16.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279078] pci 0000:00:16.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279081] pci 0000:00:16.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279083] pci 0000:00:16.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279087] pci 0000:00:16.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279089] pci 0000:00:16.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279092] pci 0000:00:16.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279095] pci 0000:00:16.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279098] pci 0000:00:16.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279100] pci 0000:00:16.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279103] pci 0000:00:15.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279106] pci 0000:00:15.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279109] pci 0000:00:15.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279111] pci 0000:00:15.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279114] pci 0000:00:15.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279117] pci 0000:00:15.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279120] pci 0000:00:15.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279122] pci 0000:00:15.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279126] pci 0000:00:15.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279128] pci 0000:00:15.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.279134] pci 0000:00:01.0: PCI bridge to [bus 01]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280667] pci 0000:02:01.0: BAR 6: assigned [mem 0xfd500000-0xfd50ffff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280679] pci 0000:02:04.0: BAR 6: assigned [mem 0xfd510000-0xfd51ffff pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280685] pci 0000:00:11.0: PCI bridge to [bus 02]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280727] pci 0000:00:11.0:   bridge window [io  0x2000-0x3fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280817] pci 0000:00:11.0:   bridge window [mem 0xfd500000-0xfdffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280865] pci 0000:00:11.0:   bridge window [mem 0xe7b00000-0xe7ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280955] pci 0000:00:15.0: PCI bridge to [bus 03]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.280991] pci 0000:00:15.0:   bridge window [io  0x4000-0x4fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.281059] pci 0000:00:15.0:   bridge window [mem 0xfd400000-0xfd4fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.281106] pci 0000:00:15.0:   bridge window [mem 0xe7a00000-0xe7afffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.281323] pci 0000:00:15.1: PCI bridge to [bus 04]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.281379] pci 0000:00:15.1:   bridge window [io  0x8000-0x8fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.281509] pci 0000:00:15.1:   bridge window [mem 0xfd000000-0xfd0fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.281614] pci 0000:00:15.1:   bridge window [mem 0xe7600000-0xe76fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.282493] pci 0000:00:15.2: PCI bridge to [bus 05]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.282536] pci 0000:00:15.2:   bridge window [io  0xc000-0xcfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.282608] pci 0000:00:15.2:   bridge window [mem 0xfcc00000-0xfccfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.282656] pci 0000:00:15.2:   bridge window [mem 0xe7200000-0xe72fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.282814] pci 0000:00:15.3: PCI bridge to [bus 06]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.282885] pci 0000:00:15.3:   bridge window [mem 0xfc800000-0xfc8fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.282932] pci 0000:00:15.3:   bridge window [mem 0xe6e00000-0xe6efffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.283068] pci 0000:00:15.4: PCI bridge to [bus 07]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.283138] pci 0000:00:15.4:   bridge window [mem 0xfc400000-0xfc4fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.283185] pci 0000:00:15.4:   bridge window [mem 0xe6a00000-0xe6afffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.283321] pci 0000:00:15.5: PCI bridge to [bus 08]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.283684] pci 0000:00:15.5:   bridge window [mem 0xfc000000-0xfc0fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.283822] pci 0000:00:15.5:   bridge window [mem 0xe6600000-0xe66fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286312] pci 0000:00:15.6: PCI bridge to [bus 09]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286391] pci 0000:00:15.6:   bridge window [mem 0xfbc00000-0xfbcfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286438] pci 0000:00:15.6:   bridge window [mem 0xe6200000-0xe62fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286573] pci 0000:00:15.7: PCI bridge to [bus 0a]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286643] pci 0000:00:15.7:   bridge window [mem 0xfb800000-0xfb8fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286689] pci 0000:00:15.7:   bridge window [mem 0xe5e00000-0xe5efffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286824] pci 0000:00:16.0: PCI bridge to [bus 0b]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286852] pci 0000:00:16.0:   bridge window [io  0x5000-0x5fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286921] pci 0000:00:16.0:   bridge window [mem 0xfd300000-0xfd3fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.286967] pci 0000:00:16.0:   bridge window [mem 0xe7900000-0xe79fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287101] pci 0000:00:16.1: PCI bridge to [bus 0c]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287129] pci 0000:00:16.1:   bridge window [io  0x9000-0x9fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287196] pci 0000:00:16.1:   bridge window [mem 0xfcf00000-0xfcffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287242] pci 0000:00:16.1:   bridge window [mem 0xe7500000-0xe75fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287374] pci 0000:00:16.2: PCI bridge to [bus 0d]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287401] pci 0000:00:16.2:   bridge window [io  0xd000-0xdfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287469] pci 0000:00:16.2:   bridge window [mem 0xfcb00000-0xfcbfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287515] pci 0000:00:16.2:   bridge window [mem 0xe7100000-0xe71fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287646] pci 0000:00:16.3: PCI bridge to [bus 0e]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287716] pci 0000:00:16.3:   bridge window [mem 0xfc700000-0xfc7fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287762] pci 0000:00:16.3:   bridge window [mem 0xe6d00000-0xe6dfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287893] pci 0000:00:16.4: PCI bridge to [bus 0f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.287992] pci 0000:00:16.4:   bridge window [mem 0xfc300000-0xfc3fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.288039] pci 0000:00:16.4:   bridge window [mem 0xe6900000-0xe69fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.288183] pci 0000:00:16.5: PCI bridge to [bus 10]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.288253] pci 0000:00:16.5:   bridge window [mem 0xfbf00000-0xfbffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.288299] pci 0000:00:16.5:   bridge window [mem 0xe6500000-0xe65fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.288433] pci 0000:00:16.6: PCI bridge to [bus 11]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.288503] pci 0000:00:16.6:   bridge window [mem 0xfbb00000-0xfbbfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.288549] pci 0000:00:16.6:   bridge window [mem 0xe6100000-0xe61fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290257] pci 0000:00:16.7: PCI bridge to [bus 12]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290339] pci 0000:00:16.7:   bridge window [mem 0xfb700000-0xfb7fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290387] pci 0000:00:16.7:   bridge window [mem 0xe5d00000-0xe5dfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290560] pci 0000:00:17.0: PCI bridge to [bus 13]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290588] pci 0000:00:17.0:   bridge window [io  0x6000-0x6fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290656] pci 0000:00:17.0:   bridge window [mem 0xfd200000-0xfd2fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290703] pci 0000:00:17.0:   bridge window [mem 0xe7800000-0xe78fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290842] pci 0000:00:17.1: PCI bridge to [bus 14]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290869] pci 0000:00:17.1:   bridge window [io  0xa000-0xafff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290937] pci 0000:00:17.1:   bridge window [mem 0xfce00000-0xfcefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.290983] pci 0000:00:17.1:   bridge window [mem 0xe7400000-0xe74fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291120] pci 0000:00:17.2: PCI bridge to [bus 15]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291147] pci 0000:00:17.2:   bridge window [io  0xe000-0xefff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291215] pci 0000:00:17.2:   bridge window [mem 0xfca00000-0xfcafffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291261] pci 0000:00:17.2:   bridge window [mem 0xe7000000-0xe70fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291395] pci 0000:00:17.3: PCI bridge to [bus 16]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291465] pci 0000:00:17.3:   bridge window [mem 0xfc600000-0xfc6fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291511] pci 0000:00:17.3:   bridge window [mem 0xe6c00000-0xe6cfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291646] pci 0000:00:17.4: PCI bridge to [bus 17]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291716] pci 0000:00:17.4:   bridge window [mem 0xfc200000-0xfc2fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291763] pci 0000:00:17.4:   bridge window [mem 0xe6800000-0xe68fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291897] pci 0000:00:17.5: PCI bridge to [bus 18]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.291993] pci 0000:00:17.5:   bridge window [mem 0xfbe00000-0xfbefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.294385] pci 0000:00:17.5:   bridge window [mem 0xe6400000-0xe64fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.294566] pci 0000:00:17.6: PCI bridge to [bus 19]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.294639] pci 0000:00:17.6:   bridge window [mem 0xfba00000-0xfbafffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.294686] pci 0000:00:17.6:   bridge window [mem 0xe6000000-0xe60fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.294823] pci 0000:00:17.7: PCI bridge to [bus 1a]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.294893] pci 0000:00:17.7:   bridge window [mem 0xfb600000-0xfb6fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.294940] pci 0000:00:17.7:   bridge window [mem 0xe5c00000-0xe5cfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295073] pci 0000:00:18.0: PCI bridge to [bus 1b]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295100] pci 0000:00:18.0:   bridge window [io  0x7000-0x7fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295168] pci 0000:00:18.0:   bridge window [mem 0xfd100000-0xfd1fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295215] pci 0000:00:18.0:   bridge window [mem 0xe7700000-0xe77fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295348] pci 0000:00:18.1: PCI bridge to [bus 1c]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295375] pci 0000:00:18.1:   bridge window [io  0xb000-0xbfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295443] pci 0000:00:18.1:   bridge window [mem 0xfcd00000-0xfcdfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295489] pci 0000:00:18.1:   bridge window [mem 0xe7300000-0xe73fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295624] pci 0000:00:18.2: PCI bridge to [bus 1d]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295694] pci 0000:00:18.2:   bridge window [mem 0xfc900000-0xfc9fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295740] pci 0000:00:18.2:   bridge window [mem 0xe6f00000-0xe6ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295874] pci 0000:00:18.3: PCI bridge to [bus 1e]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.295964] pci 0000:00:18.3:   bridge window [mem 0xfc500000-0xfc5fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.296011] pci 0000:00:18.3:   bridge window [mem 0xe6b00000-0xe6bfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.296149] pci 0000:00:18.4: PCI bridge to [bus 1f]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.296219] pci 0000:00:18.4:   bridge window [mem 0xfc100000-0xfc1fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.296265] pci 0000:00:18.4:   bridge window [mem 0xe6700000-0xe67fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297327] pci 0000:00:18.5: PCI bridge to [bus 20]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297396] pci 0000:00:18.5:   bridge window [mem 0xfbd00000-0xfbdfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297443] pci 0000:00:18.5:   bridge window [mem 0xe6300000-0xe63fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297584] pci 0000:00:18.6: PCI bridge to [bus 21]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297653] pci 0000:00:18.6:   bridge window [mem 0xfb900000-0xfb9fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297700] pci 0000:00:18.6:   bridge window [mem 0xe5f00000-0xe5ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297834] pci 0000:00:18.7: PCI bridge to [bus 22]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297903] pci 0000:00:18.7:   bridge window [mem 0xfb500000-0xfb5fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.297950] pci 0000:00:18.7:   bridge window [mem 0xe5b00000-0xe5bfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298084] pci_bus 0000:00: resource 4 [mem 0x000a0000-0x000bffff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298089] pci_bus 0000:00: resource 5 [mem 0x000d0000-0x000dbfff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298092] pci_bus 0000:00: resource 6 [mem 0xc0000000-0xfebfffff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298095] pci_bus 0000:00: resource 7 [io  0x0000-0x0cf7 window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298098] pci_bus 0000:00: resource 8 [io  0x0d00-0xfeff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298102] pci_bus 0000:02: resource 0 [io  0x2000-0x3fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298104] pci_bus 0000:02: resource 1 [mem 0xfd500000-0xfdffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298107] pci_bus 0000:02: resource 2 [mem 0xe7b00000-0xe7ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298109] pci_bus 0000:02: resource 4 [mem 0x000a0000-0x000bffff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298112] pci_bus 0000:02: resource 5 [mem 0x000d0000-0x000dbfff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298114] pci_bus 0000:02: resource 6 [mem 0xc0000000-0xfebfffff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298117] pci_bus 0000:02: resource 7 [io  0x0000-0x0cf7 window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298120] pci_bus 0000:02: resource 8 [io  0x0d00-0xfeff window]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298123] pci_bus 0000:03: resource 0 [io  0x4000-0x4fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298125] pci_bus 0000:03: resource 1 [mem 0xfd400000-0xfd4fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298128] pci_bus 0000:03: resource 2 [mem 0xe7a00000-0xe7afffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298131] pci_bus 0000:04: resource 0 [io  0x8000-0x8fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298133] pci_bus 0000:04: resource 1 [mem 0xfd000000-0xfd0fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298136] pci_bus 0000:04: resource 2 [mem 0xe7600000-0xe76fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298139] pci_bus 0000:05: resource 0 [io  0xc000-0xcfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298141] pci_bus 0000:05: resource 1 [mem 0xfcc00000-0xfccfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298143] pci_bus 0000:05: resource 2 [mem 0xe7200000-0xe72fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298146] pci_bus 0000:06: resource 1 [mem 0xfc800000-0xfc8fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298148] pci_bus 0000:06: resource 2 [mem 0xe6e00000-0xe6efffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298151] pci_bus 0000:07: resource 1 [mem 0xfc400000-0xfc4fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298154] pci_bus 0000:07: resource 2 [mem 0xe6a00000-0xe6afffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298157] pci_bus 0000:08: resource 1 [mem 0xfc000000-0xfc0fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298159] pci_bus 0000:08: resource 2 [mem 0xe6600000-0xe66fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298162] pci_bus 0000:09: resource 1 [mem 0xfbc00000-0xfbcfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298164] pci_bus 0000:09: resource 2 [mem 0xe6200000-0xe62fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298167] pci_bus 0000:0a: resource 1 [mem 0xfb800000-0xfb8fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298169] pci_bus 0000:0a: resource 2 [mem 0xe5e00000-0xe5efffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298172] pci_bus 0000:0b: resource 0 [io  0x5000-0x5fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298174] pci_bus 0000:0b: resource 1 [mem 0xfd300000-0xfd3fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298201] pci_bus 0000:0b: resource 2 [mem 0xe7900000-0xe79fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298205] pci_bus 0000:0c: resource 0 [io  0x9000-0x9fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298207] pci_bus 0000:0c: resource 1 [mem 0xfcf00000-0xfcffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298209] pci_bus 0000:0c: resource 2 [mem 0xe7500000-0xe75fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298212] pci_bus 0000:0d: resource 0 [io  0xd000-0xdfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298214] pci_bus 0000:0d: resource 1 [mem 0xfcb00000-0xfcbfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298217] pci_bus 0000:0d: resource 2 [mem 0xe7100000-0xe71fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298220] pci_bus 0000:0e: resource 1 [mem 0xfc700000-0xfc7fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298222] pci_bus 0000:0e: resource 2 [mem 0xe6d00000-0xe6dfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298225] pci_bus 0000:0f: resource 1 [mem 0xfc300000-0xfc3fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298227] pci_bus 0000:0f: resource 2 [mem 0xe6900000-0xe69fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298230] pci_bus 0000:10: resource 1 [mem 0xfbf00000-0xfbffffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298232] pci_bus 0000:10: resource 2 [mem 0xe6500000-0xe65fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298235] pci_bus 0000:11: resource 1 [mem 0xfbb00000-0xfbbfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298237] pci_bus 0000:11: resource 2 [mem 0xe6100000-0xe61fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298240] pci_bus 0000:12: resource 1 [mem 0xfb700000-0xfb7fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298242] pci_bus 0000:12: resource 2 [mem 0xe5d00000-0xe5dfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298245] pci_bus 0000:13: resource 0 [io  0x6000-0x6fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298248] pci_bus 0000:13: resource 1 [mem 0xfd200000-0xfd2fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298250] pci_bus 0000:13: resource 2 [mem 0xe7800000-0xe78fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298255] pci_bus 0000:14: resource 0 [io  0xa000-0xafff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298257] pci_bus 0000:14: resource 1 [mem 0xfce00000-0xfcefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298259] pci_bus 0000:14: resource 2 [mem 0xe7400000-0xe74fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298262] pci_bus 0000:15: resource 0 [io  0xe000-0xefff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298264] pci_bus 0000:15: resource 1 [mem 0xfca00000-0xfcafffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298266] pci_bus 0000:15: resource 2 [mem 0xe7000000-0xe70fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298269] pci_bus 0000:16: resource 1 [mem 0xfc600000-0xfc6fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298271] pci_bus 0000:16: resource 2 [mem 0xe6c00000-0xe6cfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298274] pci_bus 0000:17: resource 1 [mem 0xfc200000-0xfc2fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298276] pci_bus 0000:17: resource 2 [mem 0xe6800000-0xe68fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298279] pci_bus 0000:18: resource 1 [mem 0xfbe00000-0xfbefffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298281] pci_bus 0000:18: resource 2 [mem 0xe6400000-0xe64fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298284] pci_bus 0000:19: resource 1 [mem 0xfba00000-0xfbafffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298286] pci_bus 0000:19: resource 2 [mem 0xe6000000-0xe60fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298289] pci_bus 0000:1a: resource 1 [mem 0xfb600000-0xfb6fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298291] pci_bus 0000:1a: resource 2 [mem 0xe5c00000-0xe5cfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298294] pci_bus 0000:1b: resource 0 [io  0x7000-0x7fff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298297] pci_bus 0000:1b: resource 1 [mem 0xfd100000-0xfd1fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298299] pci_bus 0000:1b: resource 2 [mem 0xe7700000-0xe77fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298302] pci_bus 0000:1c: resource 0 [io  0xb000-0xbfff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298304] pci_bus 0000:1c: resource 1 [mem 0xfcd00000-0xfcdfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298306] pci_bus 0000:1c: resource 2 [mem 0xe7300000-0xe73fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298317] pci_bus 0000:1d: resource 1 [mem 0xfc900000-0xfc9fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298320] pci_bus 0000:1d: resource 2 [mem 0xe6f00000-0xe6ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298322] pci_bus 0000:1e: resource 1 [mem 0xfc500000-0xfc5fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298325] pci_bus 0000:1e: resource 2 [mem 0xe6b00000-0xe6bfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298327] pci_bus 0000:1f: resource 1 [mem 0xfc100000-0xfc1fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298330] pci_bus 0000:1f: resource 2 [mem 0xe6700000-0xe67fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298332] pci_bus 0000:20: resource 1 [mem 0xfbd00000-0xfbdfffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298334] pci_bus 0000:20: resource 2 [mem 0xe6300000-0xe63fffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298337] pci_bus 0000:21: resource 1 [mem 0xfb900000-0xfb9fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298339] pci_bus 0000:21: resource 2 [mem 0xe5f00000-0xe5ffffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298342] pci_bus 0000:22: resource 1 [mem 0xfb500000-0xfb5fffff]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298344] pci_bus 0000:22: resource 2 [mem 0xe5b00000-0xe5bfffff 64bit pref]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.298796] pci 0000:00:00.0: Limiting direct PCI/PCI transfers
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.305438] pci 0000:02:01.0: CLS mismatch (32 != 64), using 64 bytes
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.307064] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.307068] software IO TLB: mapped [mem 0x00000000bbed0000-0x00000000bfed0000] (64MB)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.307202] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x22df12c5959, max_idle_ns: 440795242016 ns
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.310546] clocksource: Switched to clocksource tsc
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.310612] Trying to unpack rootfs image as initramfs...
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.314220] Initialise system trusted keyrings
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.314239] Key type blacklist registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.314764] workingset: timestamp_bits=36 max_order=20 bucket_order=0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.314804] zbud: loaded
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.315381] squashfs: version 4.0 (2009/01/31) Phillip Lougher
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.315820] fuse: init (API version 7.38)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.317946] integrity: Platform Keyring initialized
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.317954] integrity: Machine keyring initialized
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.334747] Key type asymmetric registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.334755] Asymmetric key parser 'x509' registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.334868] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 243)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.335646] io scheduler mq-deadline registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.338212] pcieport 0000:00:15.0: PME: Signaling with IRQ 24
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.338389] pcieport 0000:00:15.0: pciehp: Slot #160 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.342868] pcieport 0000:00:15.1: PME: Signaling with IRQ 25
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.343059] pcieport 0000:00:15.1: pciehp: Slot #161 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.345466] pcieport 0000:00:15.2: PME: Signaling with IRQ 26
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.345617] pcieport 0000:00:15.2: pciehp: Slot #162 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.348816] pcieport 0000:00:15.3: PME: Signaling with IRQ 27
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.348997] pcieport 0000:00:15.3: pciehp: Slot #163 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.351702] pcieport 0000:00:15.4: PME: Signaling with IRQ 28
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.351881] pcieport 0000:00:15.4: pciehp: Slot #164 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.354647] pcieport 0000:00:15.5: PME: Signaling with IRQ 29
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.354819] pcieport 0000:00:15.5: pciehp: Slot #165 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.358076] pcieport 0000:00:15.6: PME: Signaling with IRQ 30
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.358294] pcieport 0000:00:15.6: pciehp: Slot #166 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.361319] pcieport 0000:00:15.7: PME: Signaling with IRQ 31
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.361504] pcieport 0000:00:15.7: pciehp: Slot #167 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.364550] pcieport 0000:00:16.0: PME: Signaling with IRQ 32
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.364773] pcieport 0000:00:16.0: pciehp: Slot #192 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.368473] pcieport 0000:00:16.1: PME: Signaling with IRQ 33
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.368656] pcieport 0000:00:16.1: pciehp: Slot #193 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.371127] pcieport 0000:00:16.2: PME: Signaling with IRQ 34
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.372413] pcieport 0000:00:16.2: pciehp: Slot #194 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.375131] pcieport 0000:00:16.3: PME: Signaling with IRQ 35
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.375330] pcieport 0000:00:16.3: pciehp: Slot #195 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.377817] pcieport 0000:00:16.4: PME: Signaling with IRQ 36
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.377988] pcieport 0000:00:16.4: pciehp: Slot #196 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.381762] pcieport 0000:00:16.5: PME: Signaling with IRQ 37
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.381950] pcieport 0000:00:16.5: pciehp: Slot #197 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.385373] pcieport 0000:00:16.6: PME: Signaling with IRQ 38
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.385587] pcieport 0000:00:16.6: pciehp: Slot #198 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.388693] pcieport 0000:00:16.7: PME: Signaling with IRQ 39
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.389905] pcieport 0000:00:16.7: pciehp: Slot #199 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.394129] pcieport 0000:00:17.0: PME: Signaling with IRQ 40
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.394349] pcieport 0000:00:17.0: pciehp: Slot #224 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.398186] pcieport 0000:00:17.1: PME: Signaling with IRQ 41
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.398365] pcieport 0000:00:17.1: pciehp: Slot #225 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.401214] pcieport 0000:00:17.2: PME: Signaling with IRQ 42
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.401408] pcieport 0000:00:17.2: pciehp: Slot #226 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.404013] pcieport 0000:00:17.3: PME: Signaling with IRQ 43
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.404189] pcieport 0000:00:17.3: pciehp: Slot #227 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.406717] pcieport 0000:00:17.4: PME: Signaling with IRQ 44
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.406770] pcieport 0000:00:17.4: pciehp: Slot #228 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.414347] pcieport 0000:00:17.5: PME: Signaling with IRQ 45
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.414526] pcieport 0000:00:17.5: pciehp: Slot #229 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.417424] pcieport 0000:00:17.6: PME: Signaling with IRQ 46
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.417613] pcieport 0000:00:17.6: pciehp: Slot #230 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.420292] pcieport 0000:00:17.7: PME: Signaling with IRQ 47
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.420468] pcieport 0000:00:17.7: pciehp: Slot #231 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.424295] pcieport 0000:00:18.0: PME: Signaling with IRQ 48
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.424679] pcieport 0000:00:18.0: pciehp: Slot #256 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.427322] pcieport 0000:00:18.1: PME: Signaling with IRQ 49
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.427493] pcieport 0000:00:18.1: pciehp: Slot #257 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.430124] pcieport 0000:00:18.2: PME: Signaling with IRQ 50
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.430309] pcieport 0000:00:18.2: pciehp: Slot #258 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.433530] pcieport 0000:00:18.3: PME: Signaling with IRQ 51
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.433699] pcieport 0000:00:18.3: pciehp: Slot #259 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.436905] pcieport 0000:00:18.4: PME: Signaling with IRQ 52
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.437138] pcieport 0000:00:18.4: pciehp: Slot #260 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.439822] pcieport 0000:00:18.5: PME: Signaling with IRQ 53
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.440127] pcieport 0000:00:18.5: pciehp: Slot #261 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.444857] pcieport 0000:00:18.6: PME: Signaling with IRQ 54
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.445052] pcieport 0000:00:18.6: pciehp: Slot #262 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.448938] pcieport 0000:00:18.7: PME: Signaling with IRQ 55
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.449129] pcieport 0000:00:18.7: pciehp: Slot #263 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.450818] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.451742] ACPI: AC: AC Adapter [ACAD] (on-line)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.451982] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.452297] ACPI: button: Power Button [PWRF]
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.455972] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.483640] 00:05: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.596527] Linux agpgart interface v0.103
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.596719] agpgart-intel 0000:00:00.0: Intel 440BX Chipset
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.599629] agpgart-intel 0000:00:00.0: AGP aperture is 256M @ 0x0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.619943] loop: module loaded
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.620740] ata_piix 0000:00:07.1: version 2.13
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.622430] scsi host0: ata_piix
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.624015] scsi host1: ata_piix
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.624146] ata1: PATA max UDMA/33 cmd 0x1f0 ctl 0x3f6 bmdma 0x1060 irq 14
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.624151] ata2: PATA max UDMA/33 cmd 0x170 ctl 0x376 bmdma 0x1068 irq 15
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.624520] tun: Universal TUN/TAP device driver, 1.6
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.624804] PPP generic driver version 2.4.2
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.626134] uhci_hcd 0000:02:00.0: UHCI Host Controller
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.626147] uhci_hcd 0000:02:00.0: new USB bus registered, assigned bus number 1
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.626249] uhci_hcd 0000:02:00.0: detected 2 ports
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.628919] uhci_hcd 0000:02:00.0: irq 18, io port 0x00002080
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.632262] usb usb1: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 6.05
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.632271] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.632275] usb usb1: Product: UHCI Host Controller
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.632278] usb usb1: Manufacturer: Linux 6.5.0-18-generic uhci_hcd
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.632280] usb usb1: SerialNumber: 0000:02:00.0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.634092] hub 1-0:1.0: USB hub found
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.634107] hub 1-0:1.0: 2 ports detected
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.634557] ehci-pci 0000:02:03.0: EHCI Host Controller
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.634570] ehci-pci 0000:02:03.0: new USB bus registered, assigned bus number 2
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.634633] i8042: PNP: PS/2 Controller [PNP0303:KBC,PNP0f13:MOUS] at 0x60,0x64 irq 1,12
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.635119] ehci-pci 0000:02:03.0: irq 17, io mem 0xfd5ef000
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.636158] serio: i8042 KBD port at 0x60,0x64 irq 1
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.636171] serio: i8042 AUX port at 0x60,0x64 irq 12
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.636757] mousedev: PS/2 mouse device common for all mice
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.638669] rtc_cmos 00:01: registered as rtc0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.638871] rtc_cmos 00:01: setting system clock to 2026-06-30T09:29:17 UTC (1782811757)
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.639071] rtc_cmos 00:01: alarms up to one month, y3k, 114 bytes nvram
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.639092] i2c_dev: i2c /dev entries driver
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.639135] device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.639163] device-mapper: uevent: version 1.0.3
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.639877] device-mapper: ioctl: 4.48.0-ioctl (2023-03-01) initialised: dm-devel@redhat.com
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640161] platform eisa.0: Probing EISA bus 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640168] platform eisa.0: EISA: Cannot allocate resource for mainboard
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640171] platform eisa.0: Cannot allocate resource for EISA slot 1
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640173] platform eisa.0: Cannot allocate resource for EISA slot 2
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640176] platform eisa.0: Cannot allocate resource for EISA slot 3
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640178] platform eisa.0: Cannot allocate resource for EISA slot 4
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640180] platform eisa.0: Cannot allocate resource for EISA slot 5
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640182] platform eisa.0: Cannot allocate resource for EISA slot 6
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640184] platform eisa.0: Cannot allocate resource for EISA slot 7
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640186] platform eisa.0: Cannot allocate resource for EISA slot 8
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640188] platform eisa.0: EISA: Detected 0 cards
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.640192] intel_pstate: CPU model not supported
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.646255] ledtrig-cpu: registered to indicate activity on CPUs
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.646756] drop_monitor: Initializing network drop monitor service
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650134] ehci-pci 0000:02:03.0: USB 2.0 started, EHCI 1.00
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650283] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.05
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650289] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650292] usb usb2: Product: EHCI Host Controller
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650294] usb usb2: Manufacturer: Linux 6.5.0-18-generic ehci_hcd
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650297] usb usb2: SerialNumber: 0000:02:03.0
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650552] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input1
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.650709] hub 2-0:1.0: USB hub found
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.651084] hub 2-0:1.0: 6 ports detected
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.681889] NET: Registered PF_INET6 protocol family
Jun 30 05:29:39 ty-virtual-machine kernel: [    1.880197] usb 1-1: new full-speed USB device number 2 using uhci_hcd
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.045814] usb 1-1: New USB device found, idVendor=0e0f, idProduct=0003, bcdDevice= 1.03
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.045829] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.045833] usb 1-1: Product: VMware Virtual USB Mouse
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.045836] usb 1-1: Manufacturer: VMware
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.184047] usb 1-2: new full-speed USB device number 3 using uhci_hcd
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.357211] usb 1-2: New USB device found, idVendor=0e0f, idProduct=0002, bcdDevice= 1.00
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.357224] usb 1-2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.357227] usb 1-2: Product: VMware Virtual USB Hub
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.357230] usb 1-2: Manufacturer: VMware, Inc.
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.366447] hub 1-2:1.0: USB hub found
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.370015] hub 1-2:1.0: 7 ports detected
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.390078] Freeing initrd memory: 68556K
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.410418] Segment Routing with IPv6
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.410454] In-situ OAM (IOAM) with IPv6
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.410520] NET: Registered PF_PACKET protocol family
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.410855] Key type dns_resolver registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.412919] IPI shorthand broadcast: enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.416205] sched_clock: Marking stable (2400837588, 11918770)->(2528786463, -116030105)
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.417466] registered taskstats version 1
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.421668] Loading compiled-in X.509 certificates
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.423859] Loaded X.509 cert 'Build time autogenerated kernel key: a7207d837189cdb9d766e4ced6907e48f3822488'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.425097] Loaded X.509 cert 'Canonical Ltd. Live Patch Signing: 14df34d1a87cf37625abec039ef2bf521249b969'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426247] Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing: 88f752e560a1e0737e31163a466ad7b70a850c19'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426256] blacklist: Loading compiled-in revocation X.509 certificates
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426302] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing: 61482aa2830d0ab2ad5af10b7250da9033ddcef0'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426338] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2017): 242ade75ac4a15e50d50c84b0d45ff3eae707a03'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426366] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (ESM 2018): 365188c1d374d6b07c3c8f240f8ef722433d6a8b'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426392] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2019): c0746fd6c5da3ae827864651ad66ae47fe24b3e8'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426417] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v1): a8d54bbb3825cfb94fa13c9f8a594a195c107b8d'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426459] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v2): 4cf046892d6fd3c9a5b03f98d845f90851dc6a8c'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426484] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.426546] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (Ubuntu Core 2019): c1d57b8f6b743f23ee41f4f7ee292f06eecadfb9'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.431666] Key type .fscrypt registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.431671] Key type fscrypt-provisioning registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.443710] Key type encrypted registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.443719] AppArmor: AppArmor sha1 policy hashing enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.443736] ima: No TPM chip found, activating TPM-bypass!
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.443743] Loading compiled-in module X.509 certificates
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444905] Loaded X.509 cert 'Build time autogenerated kernel key: a7207d837189cdb9d766e4ced6907e48f3822488'
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444911] ima: Allocated hash algorithm: sha1
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444924] ima: No architecture policies found
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444962] evm: Initialising EVM extended attributes:
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444964] evm: security.selinux
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444966] evm: security.SMACK64
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444967] evm: security.SMACK64EXEC
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444969] evm: security.SMACK64TRANSMUTE
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444970] evm: security.SMACK64MMAP
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444971] evm: security.apparmor
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444972] evm: security.ima
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444974] evm: security.capability
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.444975] evm: HMAC attrs: 0x1
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.446060] PM:   Magic number: 14:135:476
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.446314] acpi PNP0C80:109: hash matches
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.446331] acpi PNP0C80:d4: hash matches
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.466391] RAS: Correctable Errors collector initialized.
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.466488] clk: Disabling unused clocks
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.469790] Freeing unused decrypted memory: 2036K
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.472039] Freeing unused kernel image (initmem) memory: 4792K
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.496115] Write protecting the kernel read-only data: 34816k
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.509526] Freeing unused kernel image (rodata/data gap) memory: 1156K
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544726] x86/mm: Checked W+X mappings: passed, no W+X pages found.
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544747] Run /init as init process
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544750]   with arguments:
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544753]     /init
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544755]     auto
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544757]     noprompt
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544758]     splash
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544760]   with environment:
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544761]     HOME=/
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544762]     TERM=linux
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544764]     BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544765]     find_preseed=/preseed.cfg
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544767]     priority=critical
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.544768]     locale=en_US
Jun 30 05:29:39 ty-virtual-machine kernel: [    2.976091] Floppy drive(s): fd0 is 1.44M
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.000766] FDC 0 is a post-1991 82077
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.157634] piix4_smbus 0000:00:07.3: SMBus Host Controller not enabled!
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.165837] e1000: Intel(R) PRO/1000 Network Driver
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.165844] e1000: Copyright (c) 1999-2006 Intel Corporation.
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.166976] Fusion MPT base driver 3.04.20
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.166985] Copyright (c) 1999-2008 LSI Corporation
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.169485] ahci 0000:02:04.0: version 3.0
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.173374] ahci 0000:02:04.0: AHCI 0001.0300 32 slots 30 ports 6 Gbps 0x3fffffff impl SATA mode
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.173384] ahci 0000:02:04.0: flags: 64bit ncq clo only 
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.175286] Fusion MPT SPI Host driver 3.04.20
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.178297] mptbase: ioc0: Initiating bringup
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.181492] hid: raw HID events driver (C) Jiri Kosina
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.195365] usbcore: registered new interface driver usbhid
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.195371] usbhid: USB HID core driver
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.203441] scsi host2: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.212794] scsi host3: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.217232] scsi host4: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.220066] scsi host5: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.220804] scsi host6: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.221380] scsi host7: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.222067] scsi host8: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.222712] scsi host9: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.223319] scsi host10: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.223922] scsi host11: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.224640] scsi host12: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.225215] scsi host13: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.226356] scsi host14: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.226864] scsi host15: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.227591] scsi host16: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.228185] scsi host17: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.228842] scsi host18: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.249266] scsi host19: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.250280] scsi host20: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.252214] scsi host21: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.252957] scsi host22: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.253643] scsi host23: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.254275] scsi host24: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.260811] input: VirtualPS/2 VMware VMMouse as /devices/platform/i8042/serio1/input/input4
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.268476] scsi host25: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.269356] scsi host26: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.270333] scsi host27: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.271188] scsi host28: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.272406] scsi host29: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.274300] scsi host30: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276615] scsi host31: ahci
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276793] ata3: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee100 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276799] ata4: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee180 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276801] ata5: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee200 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276803] ata6: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee280 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276806] ata7: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee300 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276808] ata8: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee380 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276810] ata9: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee400 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276812] ata10: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee480 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276814] ata11: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee500 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276817] ata12: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee580 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276819] ata13: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee600 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276821] ata14: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee680 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276823] ata15: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee700 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276825] ata16: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee780 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276827] ata17: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee800 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276829] ata18: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee880 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276831] ata19: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee900 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276833] ata20: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee980 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276835] ata21: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eea00 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276837] ata22: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eea80 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276838] ata23: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eeb00 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276840] ata24: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eeb80 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276843] ata25: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eec00 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276844] ata26: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eec80 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276846] ata27: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eed00 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276848] ata28: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eed80 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276850] ata29: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eee00 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276852] ata30: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eee80 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276854] ata31: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eef00 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.276856] ata32: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eef80 irq 56
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.304705] ioc0: LSI53C1030 B0: Capabilities={Initiator}
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.317296] input: VirtualPS/2 VMware VMMouse as /devices/platform/i8042/serio1/input/input3
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.389874] input: VMware VMware Virtual USB Mouse as /devices/pci0000:00/0000:00:11.0/0000:02:00.0/usb1/1-1/1-1:1.0/0003:0E0F:0003.0001/input/input5
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.390391] hid-generic 0003:0E0F:0003.0001: input,hidraw0: USB HID v1.10 Mouse [VMware VMware Virtual USB Mouse] on usb-0000:02:00.0-1/input0
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.568231] scsi host32: ioc0: LSI53C1030 B0, FwRev=01032920h, Ports=1, MaxQ=128, IRQ=17
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.588525] ata6: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.591221] ata3: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.591338] ata3.00: ATAPI: VMware Virtual SATA CDRW Drive, 00000001, max UDMA/33
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.591495] ata3.00: configured for UDMA/33
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.591649] ata4: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.593179] ata5: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.593629] ata9: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.593695] ata10: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.594011] scsi 2:0:0:0: CD-ROM            NECVMWar VMware SATA CD00 1.00 PQ: 0 ANSI: 5
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.594664] ata4.00: ATAPI: VMware Virtual SATA CDRW Drive, 00000001, max UDMA/33
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.595624] sr 2:0:0:0: [sr0] scsi3-mmc drive: 1x/1x writer dvd-ram cd/rw xa/form2 cdda tray
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.595629] cdrom: Uniform CD-ROM driver Revision: 3.20
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.596319] ata4.00: configured for UDMA/33
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.596495] ata13: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.596530] ata12: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.596663] ata7: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.596779] ata8: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.596820] ata11: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.599428] ata14: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.599486] ata15: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.602085] ata19: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.602202] ata17: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.602241] ata16: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.602268] ata18: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.605772] ata20: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.605809] ata21: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.607402] ata22: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.613207] ata23: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.626025] ata25: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.626069] ata24: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.628179] ata28: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.628261] ata32: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.628288] ata26: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.628393] ata27: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.628445] ata29: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.632548] ata30: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.633000] ata31: SATA link down (SStatus 0 SControl 300)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.640636] sr 2:0:0:0: Attached scsi CD-ROM sr0
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.641046] sr 2:0:0:0: Attached scsi generic sg0 type 5
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.643399] scsi 3:0:0:0: CD-ROM            NECVMWar VMware SATA CD01 1.00 PQ: 0 ANSI: 5
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.683641] e1000 0000:02:01.0 eth0: (PCI:66MHz:32-bit) 00:0c:29:20:05:75
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.683661] e1000 0000:02:01.0 eth0: Intel(R) PRO/1000 Network Connection
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.689046] sr 3:0:0:0: [sr1] scsi3-mmc drive: 1x/1x writer dvd-ram cd/rw xa/form2 cdda tray
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.724013] sr 3:0:0:0: Attached scsi CD-ROM sr1
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.724318] sr 3:0:0:0: Attached scsi generic sg1 type 5
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.749709] scsi 32:0:0:0: Direct-Access     VMware,  VMware Virtual S 1.0  PQ: 0 ANSI: 2
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.765648] scsi target32:0:0: Beginning Domain Validation
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.768029] scsi target32:0:0: Domain Validation skipping write tests
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.768035] scsi target32:0:0: Ending Domain Validation
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.768152] scsi target32:0:0: FAST-40 WIDE SCSI 80.0 MB/s ST (25 ns, offset 127)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.780575] e1000 0000:02:01.0 ens33: renamed from eth0
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.782497] sd 32:0:0:0: Attached scsi generic sg2 type 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.783086] sd 32:0:0:0: [sda] 83886080 512-byte logical blocks: (42.9 GB/40.0 GiB)
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.783326] sd 32:0:0:0: [sda] Write Protect is off
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.783334] sd 32:0:0:0: [sda] Mode Sense: 61 00 00 00
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.783812] sd 32:0:0:0: [sda] Cache data unavailable
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.783818] sd 32:0:0:0: [sda] Assuming drive cache: write through
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.799062]  sda: sda1 sda2 sda3
Jun 30 05:29:39 ty-virtual-machine kernel: [    3.800567] sd 32:0:0:0: [sda] Attached SCSI disk
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.182508] EXT4-fs (sda3): mounted filesystem 4a64a517-67dd-4c66-898a-7aec80564857 ro with ordered data mode. Quota mode: none.
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.425036] systemd[1]: Inserted module 'autofs4'
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.486808] systemd[1]: systemd 249.11-0ubuntu3.12 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.486923] systemd[1]: Detected virtualization vmware.
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.486931] systemd[1]: Detected architecture x86-64.
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.487670] systemd[1]: Hostname set to <ty-virtual-machine>.
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.494233] systemd[1]: Initializing machine ID from random generator.
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.494375] systemd[1]: Installed transient /etc/machine-id file.
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.537013] systemd[1]: memfd_create() called without MFD_EXEC or MFD_NOEXEC_SEAL set
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.613183] block sda: the capability attribute has been deprecated.
Jun 30 05:29:39 ty-virtual-machine kernel: [    4.989019] systemd[1]: Queued start job for default target Graphical Interface.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.014056] systemd[1]: Created slice Slice /system/modprobe.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.014612] systemd[1]: Created slice Slice /system/systemd-fsck.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.014917] systemd[1]: Created slice User and Session Slice.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015008] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015265] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015333] systemd[1]: Reached target User and Group Name Lookups.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015351] systemd[1]: Reached target Remote File Systems.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015366] systemd[1]: Reached target Slice Units.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015383] systemd[1]: Reached target Mounting snaps.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015412] systemd[1]: Reached target Local Verity Protected Volumes.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015596] systemd[1]: Listening on Syslog Socket.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015694] systemd[1]: Listening on fsck to fsckd communication Socket.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.015824] systemd[1]: Listening on initctl Compatibility Named Pipe.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.016074] systemd[1]: Listening on Journal Audit Socket.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.016164] systemd[1]: Listening on Journal Socket (/dev/log).
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.016462] systemd[1]: Listening on Journal Socket.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.017456] systemd[1]: Listening on udev Control Socket.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.017714] systemd[1]: Listening on udev Kernel Socket.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.019661] systemd[1]: Mounting Huge Pages File System...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.023467] systemd[1]: Mounting POSIX Message Queue File System...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.025900] systemd[1]: Mounting Kernel Debug File System...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.029453] systemd[1]: Mounting Kernel Trace File System...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.035500] systemd[1]: Starting Journal Service...
Jun 30 05:29:39 ty-virtual-machine apport[670]:  * Starting automatic crash report generation: apport
Jun 30 05:29:39 ty-virtual-machine acpid: starting up with netlink and the input layer
Jun 30 05:29:39 ty-virtual-machine acpid: 8 rules loaded
Jun 30 05:29:39 ty-virtual-machine acpid: waiting for events: event logging is off
Jun 30 05:29:39 ty-virtual-machine systemd[1]: grub-common.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine apport[670]:    ...done.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Record successful boot for GRUB.
Jun 30 05:29:39 ty-virtual-machine udisksd[711]: udisks daemon version 2.9.4 starting
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.039373] systemd[1]: Starting Set the console keyboard layout...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.044899] systemd[1]: Starting Create List of Static Device Nodes...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.047771] systemd[1]: Starting Load Kernel Module configfs...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.052238] systemd[1]: Starting Load Kernel Module drm...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.055608] systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.057909] systemd[1]: Starting Load Kernel Module fuse...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.058224] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.070095] systemd[1]: Starting Load Kernel Modules...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.072232] systemd[1]: Starting Remount Root and Kernel File Systems...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.074511] systemd[1]: Starting Coldplug All udev Devices...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.078613] systemd[1]: Mounted Huge Pages File System.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.079544] systemd[1]: Mounted POSIX Message Queue File System.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.079727] systemd[1]: Mounted Kernel Debug File System.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.079915] systemd[1]: Mounted Kernel Trace File System.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.089821] systemd[1]: Finished Create List of Static Device Nodes.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.090574] systemd[1]: modprobe@configfs.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.091145] systemd[1]: Finished Load Kernel Module configfs.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.093077] systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.100715] systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.101292] systemd[1]: modprobe@fuse.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.101735] systemd[1]: Finished Load Kernel Module fuse.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.103803] systemd[1]: Mounting FUSE Control File System...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.106379] systemd[1]: Mounting Kernel Configuration File System...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.111754] systemd[1]: Mounted FUSE Control File System.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.116079] systemd[1]: Mounted Kernel Configuration File System.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.128408] ACPI: bus type drm_connector registered
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.133388] EXT4-fs (sda3): re-mounted 4a64a517-67dd-4c66-898a-7aec80564857 r/w. Quota mode: none.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.139311] systemd[1]: modprobe@drm.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.139830] systemd[1]: Finished Load Kernel Module drm.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.140685] systemd[1]: Finished Remount Root and Kernel File Systems.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.142739] systemd[1]: Activating swap /swapfile...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.143733] systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.147415] systemd[1]: Starting Load/Save Random Seed...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.150440] systemd[1]: Starting Create System Users...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.151989] lp: driver loaded but no devices found
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.157410] Adding 3991548k swap on /swapfile.  Priority:-2 extents:9 across:4302844k FS
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.160518] systemd[1]: Activated swap /swapfile.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.161179] systemd[1]: Reached target Swaps.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.164578] systemd[1]: Finished Set the console keyboard layout.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.164776] ppdev: user-space parallel port driver
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.178655] systemd[1]: Finished Load/Save Random Seed.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.178931] systemd[1]: Condition check resulted in First Boot Complete being skipped.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.194379] systemd[1]: Finished Create System Users.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.226131] systemd[1]: Starting Create Static Device Nodes in /dev...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.227199] systemd[1]: Finished Load Kernel Modules.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.230397] systemd[1]: Starting Apply Kernel Variables...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.286276] systemd[1]: Finished Create Static Device Nodes in /dev.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.286493] systemd[1]: Reached target Preparation for Local File Systems.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.314112] systemd[1]: Mounting Mount unit for bare, revision 5...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.320159] systemd[1]: Mounting Mount unit for core22, revision 1122...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.321315] loop0: detected capacity change from 0 to 8
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.323809] loop1: detected capacity change from 0 to 151992
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.324860] systemd[1]: Mounting Mount unit for firefox, revision 3836...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.328597] loop2: detected capacity change from 0 to 546064
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.329735] systemd[1]: Mounting Mount unit for gnome-42-2204, revision 141...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.334242] systemd[1]: Mounting Mount unit for gtk-common-themes, revision 1535...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.334522] loop3: detected capacity change from 0 to 1017816
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.339113] systemd[1]: Mounting Mount unit for snap-store, revision 959...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.339508] loop4: detected capacity change from 0 to 187776
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.344155] systemd[1]: Mounting Mount unit for snapd, revision 20671...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.347594] loop5: detected capacity change from 0 to 25240
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.348262] systemd[1]: Mounting Mount unit for snapd-desktop-integration, revision 83...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.350644] loop6: detected capacity change from 0 to 82800
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.351500] systemd[1]: Starting Rule-based Manager for Device Events and Files...
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.352739] systemd[1]: Started Journal Service.
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.357087] loop7: detected capacity change from 0 to 904
Jun 30 05:29:39 ty-virtual-machine kernel: [    5.419503] systemd-journald[334]: Received client request to flush runtime journal.
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.472256] vmw_vmci 0000:00:07.7: MMIO register access is available
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.472487] vmw_vmci 0000:00:07.7: Using capabilities 0x3c
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.530545] vmwgfx 0000:00:0f.0: vgaarb: deactivate vga console
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.530894] Console: switching to colour dummy device 80x25
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.534690] vmwgfx 0000:00:0f.0: [drm] FIFO at 0x00000000fe000000 size is 8192 kiB
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.535171] vmwgfx 0000:00:0f.0: [drm] VRAM at 0x00000000e8000000 size is 131072 kiB
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.535225] vmwgfx 0000:00:0f.0: [drm] Running on SVGA version 2.
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.535249] vmwgfx 0000:00:0f.0: [drm] Capabilities: rect copy, cursor, cursor bypass, cursor bypass 2, 8bit emulation, alpha cursor, 3D, extended fifo, multimon, pitchlock, irq mask, display topology, gmr, traces, gmr2, screen object 2, command buffers, command buffers 2, gbobject, dx, hp cmd queue, no bb restriction, cap2 register, 
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.535281] vmwgfx 0000:00:0f.0: [drm] Capabilities2: grow otable, intra surface copy, dx2, gb memsize 2, screendma reg, otable ptdepth2, non ms to ms stretchblt, cursor mob, mshint, cb max size 4mb, dx3, frame type, trace full fb, extra regs, lo staging, 
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.535285] vmwgfx 0000:00:0f.0: [drm] DMA map mode: Caching DMA mappings.
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.537788] vmwgfx 0000:00:0f.0: [drm] Legacy memory limits: VRAM = 131072 kB, FIFO = 256 kB, surface = 0 kB
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.537798] vmwgfx 0000:00:0f.0: [drm] MOB limits: max mob size = 1048576 kB, max mob pages = 2097152
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.537803] vmwgfx 0000:00:0f.0: [drm] Max GMR ids is 64
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.537805] vmwgfx 0000:00:0f.0: [drm] Max number of GMR pages is 65536
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.537808] vmwgfx 0000:00:0f.0: [drm] Maximum display memory size is 262144 kiB
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.559201] vmwgfx 0000:00:0f.0: [drm] Screen Target display unit initialized
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.576257] Guest personality initialized and is active
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.585638] vmwgfx 0000:00:0f.0: [drm] Fifo max 0x00040000 min 0x00001000 cap 0x0000077f
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.586681] vmwgfx 0000:00:0f.0: [drm] Using command buffers with DMA pool.
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.586692] vmwgfx 0000:00:0f.0: [drm] Available shader model: SM_5_1X.
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.594651] [drm] Initialized vmwgfx 2.20.0 20211206 for 0000:00:0f.0 on minor 0
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.601279] VMCI host device registered (name=vmci, major=10, minor=122)
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.601290] Initialized host personality
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.637703] fbcon: vmwgfxdrmfb (fb0) is primary device
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.641222] Console: switching to colour frame buffer device 160x50
Jun 30 05:29:39 ty-virtual-machine kernel: [    6.646782] vmwgfx 0000:00:0f.0: [drm] fb0: vmwgfxdrmfb frame buffer device
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.025383] RAPL PMU: API unit is 2^-32 Joules, 0 fixed counters, 10737418240 ms ovfl timer
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.090441] cryptd: max_cpu_qlen set to 1000
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.105510] AVX2 version of gcm_enc/dec engaged.
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.106527] AES CTR mode by8 optimization enabled
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.126425] audit: type=1400 audit(1782811762.984:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=469 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.127798] audit: type=1400 audit(1782811762.984:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=469 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.381910] intel_rapl_msr: PL4 support detected.
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.467649] audit: type=1400 audit(1782811763.324:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=468 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.580454] audit: type=1400 audit(1782811763.440:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=488 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.583390] audit: type=1400 audit(1782811763.440:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=488 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.584641] audit: type=1400 audit(1782811763.440:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=488 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.739583] audit: type=1400 audit(1782811763.596:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oosplash" pid=580 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.778172] audit: type=1400 audit(1782811763.636:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="tcpdump" pid=543 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.782693] audit: type=1400 audit(1782811763.640:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=470 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [    7.783353] audit: type=1400 audit(1782811763.640:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=470 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   12.671202] kauditd_printk_skb: 10 callbacks suppressed
Jun 30 05:29:39 ty-virtual-machine kernel: [   12.671208] audit: type=1400 audit(1782811768.528:22): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince" pid=471 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   12.673799] audit: type=1400 audit(1782811768.532:23): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//sanitized_helper" pid=471 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   12.676820] audit: type=1400 audit(1782811768.532:24): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//snap_browsers" pid=471 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   12.684779] audit: type=1400 audit(1782811768.544:25): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer" pid=471 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   12.686713] audit: type=1400 audit(1782811768.544:26): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer//sanitized_helper" pid=471 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   12.692226] audit: type=1400 audit(1782811768.548:27): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-thumbnailer" pid=471 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   20.019665] audit: type=1400 audit(1782811775.876:28): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-soffice" pid=629 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   20.023535] audit: type=1400 audit(1782811775.880:29): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-soffice//gpg" pid=629 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   20.558925] audit: type=1400 audit(1782811776.416:30): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=650 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   20.560245] audit: type=1400 audit(1782811776.416:31): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/20671/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=650 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   20.941063] audit: type=1400 audit(1782811776.796:32): apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.firefox" pid=654 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   21.287306] audit: type=1400 audit(1782811777.144:33): apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.geckodriver" pid=655 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   21.340681] audit: type=1400 audit(1782811777.196:34): apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.firefox" pid=651 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   21.515370] audit: type=1400 audit(1782811777.372:35): apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.snap-store" pid=652 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   21.563243] audit: type=1400 audit(1782811777.420:36): apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.configure" pid=656 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine kernel: [   21.593016] audit: type=1400 audit(1782811777.452:37): apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.connect-plug-host-hunspell" pid=657 comm="apparmor_parser"
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started LSB: automatic crash report generation.
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] AppArmor D-Bus mediation is enabled
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Successfully called chroot().
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Successfully dropped remaining capabilities.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: No service file found in /etc/avahi/services.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Joining mDNS multicast group on interface lo.IPv6 with address ::1.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: New relevant interface lo.IPv6 for mDNS.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Joining mDNS multicast group on interface lo.IPv4 with address 127.0.0.1.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: New relevant interface lo.IPv4 for mDNS.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Network interface enumeration completed.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Registering new address record for ::1 on lo.*.
Jun 30 05:29:39 ty-virtual-machine avahi-daemon[671]: Registering new address record for 127.0.0.1 on lo.IPv4.
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.PolicyKit1' unit='polkit.service' requested by ':1.8' (uid=0 pid=687 comm="/usr/libexec/power-profiles-daemon " label="unconfined")
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting GRUB failed boot detection...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: gpu-manager.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Detect the available GPUs and deal with any system changes.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Avahi mDNS/DNS-SD Stack.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started WPA supplicant.
Jun 30 05:29:39 ty-virtual-machine wpa_supplicant[712]: Successfully initialized wpa_supplicant
Jun 30 05:29:39 ty-virtual-machine polkitd[685]: started daemon version 0.105 using authority implementation `local' version `0.105'
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Authorization Manager.
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.PolicyKit1'
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Modem Manager...
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.2755] NetworkManager (version 1.36.6) is starting... (for the first time)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.2767] Read config: /etc/NetworkManager/NetworkManager.conf (lib: 10-dns-resolved.conf, 20-connectivity-ubuntu.conf, no-mac-addr-change.conf) (run: 10-globally-managed-devices.conf) (etc: default-wifi-powersave-on.conf)
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Switcheroo Control Proxy service.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Power Profiles daemon.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Condition check resulted in Manage Sound Card State (restore and store) being skipped.
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.2839] bus-manager: acquired D-Bus service "org.freedesktop.NetworkManager"
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Save/Restore Sound Card State...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: grub-initrd-fallback.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished GRUB failed boot detection.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Network Manager.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Network.
Jun 30 05:29:39 ty-virtual-machine udisksd[711]: failed to load module mdraid: libbd_mdraid.so.2: cannot open shared object file: No such file or directory
Jun 30 05:29:39 ty-virtual-machine alsactl[758]: /usr/sbin/alsactl: load_state:1689: Cannot open /var/lib/alsa/asound.state for reading: No such file or directory
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.3256] manager[0x55c33b4a6000]: monitoring kernel firmware directory '/lib/firmware'.
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.3257] monitoring ifupdown state file '/run/network/ifstate'.
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.11' (uid=0 pid=675 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 05:29:39 ty-virtual-machine alsactl[758]: alsa-lib main.c:1412:(snd_use_case_mgr_open) error: failed to import hw:0 use case configuration -2
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Network Manager Wait Online...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting CUPS Scheduler...
Jun 30 05:29:39 ty-virtual-machine snapd-aa-prompt-listener[691]: AA Prompt listener not implemented
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting OpenVPN service...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Permit User Sessions...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: snapd.aa-prompt-listener.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine udisksd[711]: Failed to load the 'mdraid' libblockdev plugin
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Save/Restore Sound Card State.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished OpenVPN service.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Permit User Sessions.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Reached target Sound Card.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting GNOME Display Manager...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Hold until boot process finishes up...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Hostname Service...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started User Login Management.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Unattended Upgrades Shutdown.
Jun 30 05:29:39 ty-virtual-machine ModemManager[750]: <info>  ModemManager (version 1.20.0) starting in system bus...
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started CUPS Scheduler.
Jun 30 05:29:39 ty-virtual-machine accounts-daemon[667]: started daemon version 22.07.5
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Accounts Service.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started GNOME Display Manager.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Modem Manager.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Received SIGRTMIN+21 from PID 401 (plymouthd).
Jun 30 05:29:39 ty-virtual-machine systemd[1]: e2scrub_reap.service: Deactivated successfully.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished Remove Stale Online ext4 Metadata Check Snapshots.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Disk Manager.
Jun 30 05:29:39 ty-virtual-machine udisksd[711]: Acquired the name org.freedesktop.UDisks2 on the system message bus
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Hostname Service.
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.6756] hostname: hostname: using hostnamed
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.6756] hostname: static hostname changed from (none) to "ty-virtual-machine"
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.6787] dns-mgr[0x55c33b4842a0]: init: dns=systemd-resolved rc-manager=unmanaged (auto), plugin=systemd-resolved
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.6807] manager[0x55c33b4a6000]: rfkill: Wi-Fi hardware radio set enabled
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.6808] manager[0x55c33b4a6000]: rfkill: WWAN hardware radio set enabled
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.6998] Loaded device plugin: NMTeamFactory (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-team.so)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7068] Loaded device plugin: NMWwanFactory (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-wwan.so)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7082] Loaded device plugin: NMAtmManager (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-adsl.so)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7121] Loaded device plugin: NMWifiFactory (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-wifi.so)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7160] Loaded device plugin: NMBluezManager (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-bluetooth.so)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7171] manager: rfkill: Wi-Fi enabled by radio killswitch; enabled by state file
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7181] manager: rfkill: WWAN enabled by radio killswitch; enabled by state file
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7191] manager: Networking is enabled by state file
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.11' (uid=0 pid=675 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7283] settings: Loaded settings plugin: ifupdown ("/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-settings-plugin-ifupdown.so")
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7284] settings: Loaded settings plugin: keyfile (internal)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7284] ifupdown: management mode: unmanaged
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7291] ifupdown: interfaces file /etc/network/interfaces doesn't exist
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]: No valid path found for iw
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7349] dhcp-init: Using DHCP client 'internal'
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7349] device (lo): carrier: link connected
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7360] manager: (lo): new Generic device (/org/freedesktop/NetworkManager/Devices/1)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7381] manager: (ens33): new Ethernet device (/org/freedesktop/NetworkManager/Devices/2)
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7420] settings: (ens33): created default wired connection 'Wired connection 1'
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7420] device (ens33): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7638] failed to open /run/network/ifstate
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Created slice User Slice of UID 128.
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.network1' unit='dbus-org.freedesktop.network1.service' requested by ':1.19' (uid=0 pid=829 comm="/usr/bin/networkctl list --no-pager --no-legend " label="unconfined")
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting User Runtime Directory /run/user/128...
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Activation via systemd failed for unit 'dbus-org.freedesktop.network1.service': Unit dbus-org.freedesktop.network1.service not found.
Jun 30 05:29:39 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[829]: WARNING: systemd-networkd is not running, output will be incomplete.
Jun 30 05:29:39 ty-virtual-machine NetworkManager[675]: <info>  [1782811779.7951] modem-manager: ModemManager available
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]: ERROR:Unknown state for interface NetworkctlListState(idx=1, name='lo', type='loopback', operational='n/a', administrative='unmanaged'): n/a
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]: Traceback (most recent call last):
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:   File "/usr/bin/networkd-dispatcher", line 298, in trigger_all
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:     self.handle_state(iface_name,
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:   File "/usr/bin/networkd-dispatcher", line 348, in handle_state
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:     raise UnknownState(operational_state)
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]: UnknownState: n/a
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]: ERROR:Unknown state for interface NetworkctlListState(idx=2, name='ens33', type='ether', operational='n/a', administrative='unmanaged'): n/a
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]: Traceback (most recent call last):
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:   File "/usr/bin/networkd-dispatcher", line 298, in trigger_all
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:     self.handle_state(iface_name,
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:   File "/usr/bin/networkd-dispatcher", line 348, in handle_state
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]:     raise UnknownState(operational_state)
Jun 30 05:29:39 ty-virtual-machine networkd-dispatcher[683]: UnknownState: n/a
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Started Dispatcher daemon for systemd-networkd.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Finished User Runtime Directory /run/user/128.
Jun 30 05:29:39 ty-virtual-machine systemd[1]: Starting User Manager for UID 128...
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Queued start job for default target Main User Target.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Created slice User Application Slice.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Created slice User Background Tasks Slice.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Created slice User Core Session Slice.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Started Pending report trigger for Ubuntu Report.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Reached target Paths.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Reached target Timers.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Starting D-Bus User Message Bus Socket...
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on GnuPG network certificate management daemon.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on GnuPG cryptographic agent and passphrase cache.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on PipeWire Multimedia System Socket.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on debconf communication socket.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on Sound System.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on REST API socket for snapd user session agent.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on Speech Dispatcher Socket.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Listening on D-Bus User Message Bus Socket.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Reached target Sockets.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Reached target Basic System.
Jun 30 05:29:40 ty-virtual-machine systemd[1]: Started User Manager for UID 128.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Started PipeWire Multimedia Service.
Jun 30 05:29:40 ty-virtual-machine systemd[1]: Started Session c1 of User gdm.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Started PipeWire Media Session Manager.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Starting Sound Service...
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Starting Tracker metadata extractor...
Jun 30 05:29:40 ty-virtual-machine avahi-daemon[671]: Server startup complete. Host name is ty-virtual-machine.local. Local service cookie is 1795376732.
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Started D-Bus User Message Bus.
Jun 30 05:29:40 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.RealtimeKit1' unit='rtkit-daemon.service' requested by ':1.25' (uid=128 pid=850 comm="/usr/bin/pipewire-media-session " label="unconfined")
Jun 30 05:29:40 ty-virtual-machine systemd[1]: Starting RealtimeKit Scheduling Policy Service...
Jun 30 05:29:40 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.RealtimeKit1'
Jun 30 05:29:40 ty-virtual-machine systemd[1]: Started RealtimeKit Scheduling Policy Service.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully called chroot.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully dropped privileges.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully limited resources.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Running.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Watchdog thread running.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Canary thread running.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 0 threads of 0 processes of 0 users.
Jun 30 05:29:40 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] AppArmor D-Bus mediation is enabled
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 849 of process 849 owned by '128' high priority at nice level -11.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 1 threads of 1 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 851 of process 851 owned by '128' high priority at nice level -11.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 2 threads of 2 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: message repeated 2 times: [ Supervising 2 threads of 2 processes of 1 users.]
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 859 of process 850 owned by '128' RT at priority 20.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 3 threads of 3 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 3 threads of 3 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 864 of process 849 owned by '128' RT at priority 20.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 4 threads of 3 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.4' (uid=128 pid=852 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Starting Virtual filesystem service...
Jun 30 05:29:40 ty-virtual-machine gnome-session[863]: gnome-session-binary[863]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:29:40 ty-virtual-machine gnome-session-binary[863]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:29:40 ty-virtual-machine gnome-session[863]: gnome-session-binary[863]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:29:40 ty-virtual-machine gnome-session-binary[863]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:29:40 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 30 05:29:40 ty-virtual-machine systemd[836]: Started Virtual filesystem service.
Jun 30 05:29:40 ty-virtual-machine pulseaudio[851]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 4 threads of 3 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 877 of process 851 owned by '128' RT at priority 5.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 5 threads of 3 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine pulseaudio[851]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:29:40 ty-virtual-machine pulseaudio[851]: ALSA woke us up to write new data to the device, but there was actually nothing to write.
Jun 30 05:29:40 ty-virtual-machine pulseaudio[851]: Most likely this is a bug in the ALSA driver 'snd_ens1371'. Please report this issue to the ALSA developers.
Jun 30 05:29:40 ty-virtual-machine pulseaudio[851]: We were woken up with POLLOUT set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 5 threads of 3 processes of 1 users.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 882 of process 851 owned by '128' RT at priority 5.
Jun 30 05:29:40 ty-virtual-machine rtkit-daemon[856]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:29:41 ty-virtual-machine snapd[693]: overlord.go:271: Acquiring state lock file
Jun 30 05:29:41 ty-virtual-machine snapd[693]: overlord.go:276: Acquired state lock file
Jun 30 05:29:41 ty-virtual-machine gnome-shell[908]: Running GNOME Shell (using mutter 42.9) as a Wayland display server
Jun 30 05:29:41 ty-virtual-machine snapd[693]: patch.go:64: Patching system state level 6 to sublevel 1...
Jun 30 05:29:41 ty-virtual-machine snapd[693]: patch.go:64: Patching system state level 6 to sublevel 2...
Jun 30 05:29:41 ty-virtual-machine snapd[693]: patch.go:64: Patching system state level 6 to sublevel 3...
Jun 30 05:29:41 ty-virtual-machine snapd[693]: daemon.go:247: started snapd/2.61.1 (series 16; classic) ubuntu/22.04 (amd64) linux/6.5.0-18-generic.
Jun 30 05:29:41 ty-virtual-machine kernel: [   25.775301] loop8: detected capacity change from 0 to 8
Jun 30 05:29:41 ty-virtual-machine systemd[1]: tmp-syscheck\x2dmountpoint\x2d1842729202.mount: Deactivated successfully.
Jun 30 05:29:41 ty-virtual-machine snapd[693]: daemon.go:340: adjusting startup timeout by 1m10s (pessimistic estimate of 30s plus 5s per snap)
Jun 30 05:29:41 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.33' (uid=128 pid=851 comm="/usr/bin/pulseaudio --daemonize=no --log-target=jo" label="unconfined")
Jun 30 05:29:41 ty-virtual-machine pulseaudio[851]: Failed to open cookie file '/var/lib/gdm3/.config/pulse/cookie': No such file or directory
Jun 30 05:29:41 ty-virtual-machine pulseaudio[851]: Failed to load authentication key '/var/lib/gdm3/.config/pulse/cookie': No such file or directory
Jun 30 05:29:41 ty-virtual-machine pulseaudio[851]: Failed to open cookie file '/var/lib/gdm3/.pulse-cookie': No such file or directory
Jun 30 05:29:41 ty-virtual-machine pulseaudio[851]: Failed to load authentication key '/var/lib/gdm3/.pulse-cookie': No such file or directory
Jun 30 05:29:41 ty-virtual-machine systemd[1]: Condition check resulted in Bluetooth service being skipped.
Jun 30 05:29:41 ty-virtual-machine snapd[693]: backends.go:58: AppArmor status: apparmor is enabled and all features are available (using snapd provided apparmor_parser)
Jun 30 05:29:41 ty-virtual-machine systemd[836]: Started Sound Service.
Jun 30 05:29:41 ty-virtual-machine gnome-shell[908]: Added device '/dev/dri/card0' (vmwgfx) using non-atomic mode setting.
Jun 30 05:29:42 ty-virtual-machine systemd[1]: Started Snap Daemon.
Jun 30 05:29:42 ty-virtual-machine systemd[1]: Starting Wait until snapd is fully seeded...
Jun 30 05:29:42 ty-virtual-machine ModemManager[750]: <info>  [base-manager] couldn't check support for device '/sys/devices/pci0000:00/0000:00:11.0/0000:02:01.0': not supported by any plugin
Jun 30 05:29:42 ty-virtual-machine gnome-shell[908]: Created gbm renderer for '/dev/dri/card0'
Jun 30 05:29:42 ty-virtual-machine gnome-shell[908]: Boot VGA GPU /dev/dri/card0 selected as primary
Jun 30 05:29:42 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.a11y.Bus' requested by ':1.4' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:42 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Successfully activated service 'org.a11y.Bus'
Jun 30 05:29:42 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.4' (uid=128 pid=852 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:29:43 ty-virtual-machine systemd[836]: Starting Tracker file system data miner...
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &DOCUMENTS. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &MUSIC. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &PICTURES. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &VIDEOS. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &DOWNLOAD. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &DOCUMENTS. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &MUSIC. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &PICTURES. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine tracker-miner-f[988]: Unable to get XDG user directory path for special directory &VIDEOS. Ignoring this location.
Jun 30 05:29:43 ty-virtual-machine gnome-shell[908]: Using public X11 display :1024, (using :1025 for managed services)
Jun 30 05:29:43 ty-virtual-machine gnome-shell[908]: Using Wayland display name 'wayland-0'
Jun 30 05:29:43 ty-virtual-machine org.gnome.Shell.desktop[993]: (WW) Option "-listen" for file descriptors is deprecated
Jun 30 05:29:43 ty-virtual-machine org.gnome.Shell.desktop[993]: Please use "-listenfd" instead.
Jun 30 05:29:43 ty-virtual-machine org.gnome.Shell.desktop[993]: (WW) Option "-listen" for file descriptors is deprecated
Jun 30 05:29:43 ty-virtual-machine org.gnome.Shell.desktop[993]: Please use "-listenfd" instead.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.gtk.vfs.UDisks2VolumeMonitor' unit='gvfs-udisks2-volume-monitor.service' requested by ':1.9' (uid=128 pid=988 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Starting Virtual filesystem service - disk device monitor...
Jun 30 05:29:44 ty-virtual-machine systemd[1]: dmesg.service: Deactivated successfully.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gtk.vfs.UDisks2VolumeMonitor'
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Started Virtual filesystem service - disk device monitor.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.gtk.vfs.AfcVolumeMonitor' unit='gvfs-afc-volume-monitor.service' requested by ':1.9' (uid=128 pid=988 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Starting Virtual filesystem service - Apple File Conduit monitor...
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gtk.vfs.AfcVolumeMonitor'
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Started Virtual filesystem service - Apple File Conduit monitor.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.gtk.vfs.MTPVolumeMonitor' unit='gvfs-mtp-volume-monitor.service' requested by ':1.9' (uid=128 pid=988 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Starting Virtual filesystem service - Media Transfer Protocol monitor...
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gtk.vfs.MTPVolumeMonitor'
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Started Virtual filesystem service - Media Transfer Protocol monitor.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.gtk.vfs.GPhoto2VolumeMonitor' unit='gvfs-gphoto2-volume-monitor.service' requested by ':1.9' (uid=128 pid=988 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Starting Virtual filesystem service - digital camera monitor...
Jun 30 05:29:44 ty-virtual-machine gnome-shell[908]: Unset XDG_SESSION_ID, getCurrentSessionProxy() called outside a user session. Asking logind directly.
Jun 30 05:29:44 ty-virtual-machine gnome-shell[908]: Will monitor session c1
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gtk.vfs.GPhoto2VolumeMonitor'
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Started Virtual filesystem service - digital camera monitor.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.gtk.vfs.GoaVolumeMonitor' unit='gvfs-goa-volume-monitor.service' requested by ':1.9' (uid=128 pid=988 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.locale1' unit='dbus-org.freedesktop.locale1.service' requested by ':1.34' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Starting Virtual filesystem service - GNOME Online Accounts monitor...
Jun 30 05:29:44 ty-virtual-machine systemd[1]: Starting Locale Service...
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating service name='org.gnome.OnlineAccounts' requested by ':1.14' (uid=128 pid=1019 comm="/usr/libexec/gvfs-goa-volume-monitor " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.locale1'
Jun 30 05:29:44 ty-virtual-machine systemd[1]: Started Locale Service.
Jun 30 05:29:44 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.freedesktop.impl.portal.PermissionStore' requested by ':1.3' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine goa-daemon[1024]: goa-daemon version 3.44.0 starting
Jun 30 05:29:44 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating service name='org.gnome.Identity' requested by ':1.15' (uid=128 pid=1024 comm="/usr/libexec/goa-daemon " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gnome.OnlineAccounts'
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gtk.vfs.GoaVolumeMonitor'
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Started Virtual filesystem service - GNOME Online Accounts monitor.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.UPower' unit='upower.service' requested by ':1.38' (uid=128 pid=988 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.gnome.Identity'
Jun 30 05:29:44 ty-virtual-machine systemd[1]: Starting Daemon for power management...
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.UPower'
Jun 30 05:29:44 ty-virtual-machine systemd[1]: Started Daemon for power management.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.freedesktop.Tracker3.Miner.Files'
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Started Tracker file system data miner.
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Started Tracker metadata extractor.
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Reached target Main User Target.
Jun 30 05:29:44 ty-virtual-machine systemd[836]: Startup finished in 4.994s.
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.GeoClue2' unit='geoclue.service' requested by ':1.34' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:44 ty-virtual-machine systemd[1]: Starting Location Lookup Service...
Jun 30 05:29:44 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.PackageKit' unit='packagekit.service' requested by ':1.34' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Starting PackageKit Daemon...
Jun 30 05:29:45 ty-virtual-machine gnome-shell[908]: Extension ding@rastersoft.com already installed in /usr/share/gnome-shell/extensions/ding@rastersoft.com. /usr/share/gnome-shell/extensions/ding@rastersoft.com will not be loaded
Jun 30 05:29:45 ty-virtual-machine gnome-shell[908]: Extension ubuntu-appindicators@ubuntu.com already installed in /usr/share/gnome-shell/extensions/ubuntu-appindicators@ubuntu.com. /usr/share/gnome-shell/extensions/ubuntu-appindicators@ubuntu.com will not be loaded
Jun 30 05:29:45 ty-virtual-machine gnome-shell[908]: Extension ubuntu-dock@ubuntu.com already installed in /usr/share/gnome-shell/extensions/ubuntu-dock@ubuntu.com. /usr/share/gnome-shell/extensions/ubuntu-dock@ubuntu.com will not be loaded
Jun 30 05:29:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.gnome.Shell.Notifications' requested by ':1.3' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:45 ty-virtual-machine PackageKit: daemon start
Jun 30 05:29:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[981]: dbus-daemon[981]: Activating service name='org.a11y.atspi.Registry' requested by ':1.0' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:45 ty-virtual-machine org.gnome.Shell.desktop[908]: Window manager warning: Failed to parse saved session file: Failed to open file “/var/lib/gdm3/.config/mutter/sessions/10c5d2bf1f83acb283178281178123232700000008630000.ms”: No such file or directory
Jun 30 05:29:45 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.GeoClue2'
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Started Location Lookup Service.
Jun 30 05:29:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[981]: dbus-daemon[981]: Successfully activated service 'org.a11y.atspi.Registry'
Jun 30 05:29:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[1072]: SpiRegistry daemon is running with well-known name - org.a11y.atspi.Registry
Jun 30 05:29:45 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.PackageKit'
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Started PackageKit Daemon.
Jun 30 05:29:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.freedesktop.systemd1' requested by ':1.9' (uid=128 pid=1082 comm="/usr/libexec/gsd-sharing " label="unconfined")
Jun 30 05:29:45 ty-virtual-machine kernel: [   29.619616] rfkill: input handler disabled
Jun 30 05:29:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activated service 'org.freedesktop.systemd1' failed: Process org.freedesktop.systemd1 exited with status 1
Jun 30 05:29:45 ty-virtual-machine gsd-sharing[1082]: Failed to StopUnit service: GDBus.Error:org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
Jun 30 05:29:45 ty-virtual-machine gsd-sharing[1082]: Failed to StopUnit service: GDBus.Error:org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
Jun 30 05:29:45 ty-virtual-machine gnome-shell[908]: JS ERROR: TypeError: this._managerProxy is undefined#012_onGeoclueVanished@resource:///org/gnome/shell/ui/status/location.js:169:9
Jun 30 05:29:45 ty-virtual-machine NetworkManager[675]: <info>  [1782811785.6603] agent-manager: agent[c8cccbb86ca7db04,:1.34/org.gnome.Shell.NetworkAgent/128]: agent registered
Jun 30 05:29:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Successfully activated service 'org.gnome.Shell.Notifications'
Jun 30 05:29:45 ty-virtual-machine NetworkManager[675]: <info>  [1782811785.7576] manager: startup complete
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Finished Network Manager Wait Online.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Reached target Network is Online.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Started Download data for packages that failed at package install time.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Started Check to see whether there is a new version of Ubuntu available.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Reached target Timer Units.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Started Make remote CUPS printers available locally.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Starting Tool to automatically collect and submit kernel crash signatures...
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Condition check resulted in Ubuntu Pro Background Auto Attach being skipped.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Started crash report submission.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: kerneloops.service: Found left-over process 1203 (kerneloops) in control group while starting unit. Ignoring.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Jun 30 05:29:45 ty-virtual-machine systemd[1]: Started Tool to automatically collect and submit kernel crash signatures.
Jun 30 05:29:45 ty-virtual-machine whoopsie[1202]: [05:29:45] Using lock path: /var/lock/whoopsie/lock
Jun 30 05:29:45 ty-virtual-machine systemd[1]: whoopsie.service: Deactivated successfully.
Jun 30 05:29:45 ty-virtual-machine gnome-shell[908]: Error looking up permission: GDBus.Error:org.freedesktop.portal.Error.NotFound: No entry for geolocation
Jun 30 05:29:46 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.gtk.vfs.Daemon' requested by ':1.25' (uid=128 pid=1143 comm="ibus-daemon --panel disable " label="unconfined")
Jun 30 05:29:46 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 30 05:29:46 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.34' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:29:46 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.freedesktop.portal.IBus' requested by ':1.25' (uid=128 pid=1143 comm="ibus-daemon --panel disable " label="unconfined")
Jun 30 05:29:46 ty-virtual-machine systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 30 05:29:46 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 30 05:29:47 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 30 05:29:47 ty-virtual-machine systemd[1]: Started Fingerprint Authentication Daemon.
Jun 30 05:29:47 ty-virtual-machine fprintd[1234]: libusb: error [udev_hotplug_event] ignoring udev action change
Jun 30 05:29:47 ty-virtual-machine gnome-shell[908]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available#012asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 30 05:29:47 ty-virtual-machine systemd-udevd[1166]: Using default interface naming scheme 'v249'.
Jun 30 05:29:47 ty-virtual-machine fprintd[1234]: libusb: error [udev_hotplug_event] ignoring udev action change
Jun 30 05:29:47 ty-virtual-machine fprintd[1234]: message repeated 2 times: [ libusb: error [udev_hotplug_event] ignoring udev action change]
Jun 30 05:29:47 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.ColorManager' unit='colord.service' requested by ':1.57' (uid=128 pid=1086 comm="/usr/libexec/gsd-color " label="unconfined")
Jun 30 05:29:47 ty-virtual-machine systemd[1]: Starting Manage, Install and Generate Color Profiles...
Jun 30 05:29:47 ty-virtual-machine colord[1328]: failed to get edid data: EDID length is too small
Jun 30 05:29:47 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.ColorManager'
Jun 30 05:29:47 ty-virtual-machine systemd[1]: Started Manage, Install and Generate Color Profiles.
Jun 30 05:29:47 ty-virtual-machine spice-vdagent[1329]: vdagent virtio channel /dev/virtio-ports/com.redhat.spice.0 does not exist, exiting
Jun 30 05:29:47 ty-virtual-machine gnome-session-binary[863]: Entering running state
Jun 30 05:29:47 ty-virtual-machine xbrlapi.desktop[1336]: openConnection: connect: No such file or directory
Jun 30 05:29:47 ty-virtual-machine xbrlapi.desktop[1336]: cannot connect to braille devices daemon brltty at :0
Jun 30 05:29:47 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.gnome.ScreenSaver' requested by ':1.22' (uid=128 pid=1126 comm="/usr/libexec/gsd-power " label="unconfined")
Jun 30 05:29:47 ty-virtual-machine gsd-media-keys[1118]: Failed to grab accelerator for keybinding settings:playback-repeat
Jun 30 05:29:47 ty-virtual-machine gsd-media-keys[1118]: Failed to grab accelerator for keybinding settings:hibernate
Jun 30 05:29:47 ty-virtual-machine gnome-shell[908]: ATK Bridge is disabled but a11y has already been enabled.
Jun 30 05:29:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Successfully activated service 'org.gnome.ScreenSaver'
Jun 30 05:29:48 ty-virtual-machine gsd-color[1086]: failed to get edid: unable to get EDID for output
Jun 30 05:29:48 ty-virtual-machine gsd-color[1086]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:29:48 ty-virtual-machine org.gnome.Shell.desktop[1380]: The XKEYBOARD keymap compiler (xkbcomp) reports:
Jun 30 05:29:48 ty-virtual-machine org.gnome.Shell.desktop[1380]: > Warning:          Unsupported maximum keycode 708, clipping.
Jun 30 05:29:48 ty-virtual-machine org.gnome.Shell.desktop[1380]: >                   X11 cannot support keycodes above 255.
Jun 30 05:29:48 ty-virtual-machine org.gnome.Shell.desktop[1380]: Errors from xkbcomp are not fatal to the X server
Jun 30 05:29:48 ty-virtual-machine gnome-shell[908]: Registering session with GDM
Jun 30 05:29:48 ty-virtual-machine systemd[1]: Received SIGRTMIN+21 from PID 401 (plymouthd).
Jun 30 05:29:48 ty-virtual-machine systemd[1]: Finished Hold until boot process finishes up.
Jun 30 05:29:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Activating service name='org.freedesktop.portal.IBus' requested by ':1.36' (uid=128 pid=1372 comm="ibus-daemon --panel disable -r --xim " label="unconfined")
Jun 30 05:29:48 ty-virtual-machine systemd[1]: Starting Set console scheme...
Jun 30 05:29:48 ty-virtual-machine systemd[1]: Finished Set console scheme.
Jun 30 05:29:48 ty-virtual-machine systemd[1]: Created slice Slice /system/getty.
Jun 30 05:29:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[862]: dbus-daemon[862]: [session uid=128 pid=862] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 30 05:29:48 ty-virtual-machine kernel: [   32.828981] kauditd_printk_skb: 10 callbacks suppressed
Jun 30 05:29:48 ty-virtual-machine kernel: [   32.828987] audit: type=1400 audit(1782811788.688:48): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=1406 comm="apparmor_parser"
Jun 30 05:29:48 ty-virtual-machine kernel: [   32.844939] audit: type=1400 audit(1782811788.704:49): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/snap/snapd/20671/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=1406 comm="apparmor_parser"
Jun 30 05:29:49 ty-virtual-machine ModemManager[750]: <info>  [base-manager] couldn't check support for device '/sys/devices/pci0000:00/0000:00:11.0/0000:02:01.0': not supported by any plugin
Jun 30 05:29:49 ty-virtual-machine kernel: [   33.830541] audit: type=1400 audit(1782811789.688:50): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap-update-ns.firefox" pid=1409 comm="apparmor_parser"
Jun 30 05:29:49 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 05:29:50 ty-virtual-machine kernel: [   34.370438] audit: type=1400 audit(1782811790.228:51): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.firefox" pid=1410 comm="apparmor_parser"
Jun 30 05:29:50 ty-virtual-machine kernel: [   34.690432] audit: type=1400 audit(1782811790.548:52): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.configure" pid=1416 comm="apparmor_parser"
Jun 30 05:29:50 ty-virtual-machine kernel: [   34.935995] audit: type=1400 audit(1782811790.792:53): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.connect-plug-host-hunspell" pid=1417 comm="apparmor_parser"
Jun 30 05:29:51 ty-virtual-machine kernel: [   35.191229] audit: type=1400 audit(1782811791.048:54): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.disconnect-plug-host-hunspell" pid=1418 comm="apparmor_parser"
Jun 30 05:29:51 ty-virtual-machine kernel: [   35.325156] audit: type=1400 audit(1782811791.180:55): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.geckodriver" pid=1415 comm="apparmor_parser"
Jun 30 05:29:51 ty-virtual-machine kernel: [   35.443621] audit: type=1400 audit(1782811791.300:56): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.post-refresh" pid=1419 comm="apparmor_parser"
Jun 30 05:29:51 ty-virtual-machine systemd[1]: Started snap.firefox.hook.connect-plug-host-hunspell-a36adf82-d756-4865-8593-e013c56c50ac.scope.
Jun 30 05:29:51 ty-virtual-machine systemd[1]: tmp-snap.rootfs_3AkHms.mount: Deactivated successfully.
Jun 30 05:29:52 ty-virtual-machine kernel: [   36.243910] audit: type=1400 audit(1782811792.100:57): apparmor="DENIED" operation="open" class="file" profile="snap-update-ns.firefox" name="/usr/local/share/" pid=1437 comm="6" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Jun 30 05:29:52 ty-virtual-machine systemd[1]: systemd-fsckd.service: Deactivated successfully.
Jun 30 05:29:53 ty-virtual-machine systemd[1]: Reloading.
Jun 30 05:29:53 ty-virtual-machine systemd[1]: Mounting Mount unit for firefox, revision 3836 via mount-control...
Jun 30 05:29:53 ty-virtual-machine systemd[1]: Mounted Mount unit for firefox, revision 3836 via mount-control.
Jun 30 05:29:53 ty-virtual-machine systemd[1]: snap.firefox.hook.connect-plug-host-hunspell-a36adf82-d756-4865-8593-e013c56c50ac.scope: Deactivated successfully.
Jun 30 05:29:53 ty-virtual-machine systemd[1]: snap.firefox.hook.connect-plug-host-hunspell-a36adf82-d756-4865-8593-e013c56c50ac.scope: Consumed 1.585s CPU time.
Jun 30 05:29:54 ty-virtual-machine systemd[1]: Started snap.firefox.hook.configure-709599e0-935c-4854-80c8-fe6e3a139754.scope.
Jun 30 05:29:59 ty-virtual-machine systemd[1]: snap.firefox.hook.configure-709599e0-935c-4854-80c8-fe6e3a139754.scope: Deactivated successfully.
Jun 30 05:29:59 ty-virtual-machine systemd[1]: snap.firefox.hook.configure-709599e0-935c-4854-80c8-fe6e3a139754.scope: Consumed 2.767s CPU time.
Jun 30 05:30:00 ty-virtual-machine systemd[1]: Started snap.snap-store.hook.configure-819e5876-f6da-4466-b161-7f8150c741a3.scope.
Jun 30 05:30:00 ty-virtual-machine systemd[1]: tmp-snap.rootfs_4JmoyW.mount: Deactivated successfully.
Jun 30 05:30:00 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.9' (uid=128 pid=988 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:30:00 ty-virtual-machine systemd[836]: Starting Tracker metadata extractor...
Jun 30 05:30:00 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.freedesktop.Tracker3.Miner.Extract'
Jun 30 05:30:00 ty-virtual-machine systemd[836]: Started Tracker metadata extractor.
Jun 30 05:30:04 ty-virtual-machine systemd[1]: snap.snap-store.hook.configure-819e5876-f6da-4466-b161-7f8150c741a3.scope: Deactivated successfully.
Jun 30 05:30:04 ty-virtual-machine systemd[1]: snap.snap-store.hook.configure-819e5876-f6da-4466-b161-7f8150c741a3.scope: Consumed 2.307s CPU time.
Jun 30 05:30:04 ty-virtual-machine systemd[836]: Starting snapd user session agent...
Jun 30 05:30:04 ty-virtual-machine systemd[836]: Started snapd user session agent.
Jun 30 05:30:04 ty-virtual-machine systemd[836]: Started Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:30:04 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.freedesktop.portal.Documents' unit='xdg-document-portal.service' requested by ':1.19' (uid=128 pid=1558 comm="/usr/bin/snap run snapd-desktop-integration " label="unconfined")
Jun 30 05:30:04 ty-virtual-machine systemd[1]: Started snap.snapd-desktop-integration.hook.configure-3ba1c5b1-c9cc-4ea0-a367-af9b03987bab.scope.
Jun 30 05:30:04 ty-virtual-machine systemd[836]: Starting flatpak document portal service...
Jun 30 05:30:04 ty-virtual-machine systemd[1]: tmp-snap.rootfs_haGHtl.mount: Deactivated successfully.
Jun 30 05:30:04 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Activating via systemd: service name='org.freedesktop.impl.portal.PermissionStore' unit='xdg-permission-store.service' requested by ':1.20' (uid=128 pid=1595 comm="/usr/libexec/xdg-document-portal " label="unconfined")
Jun 30 05:30:04 ty-virtual-machine systemd[836]: Starting sandboxed app permission store...
Jun 30 05:30:04 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 30 05:30:04 ty-virtual-machine systemd[836]: Started sandboxed app permission store.
Jun 30 05:30:05 ty-virtual-machine dbus-daemon[855]: [session uid=128 pid=855] Successfully activated service 'org.freedesktop.portal.Documents'
Jun 30 05:30:05 ty-virtual-machine systemd[836]: Started flatpak document portal service.
Jun 30 05:30:05 ty-virtual-machine kernel: [   49.290128] kauditd_printk_skb: 2 callbacks suppressed
Jun 30 05:30:05 ty-virtual-machine kernel: [   49.290133] audit: type=1400 audit(1782811805.148:60): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=1558 comm="snap-confine" capability=12  capname="net_admin"
Jun 30 05:30:05 ty-virtual-machine kernel: [   49.290145] audit: type=1400 audit(1782811805.148:61): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=1558 comm="snap-confine" capability=38  capname="perfmon"
Jun 30 05:30:05 ty-virtual-machine snapd-desktop-integration.snapd-desktop-integration[1558]: Sorry, home directories outside of /home needs configuration.
Jun 30 05:30:05 ty-virtual-machine snapd-desktop-integration.snapd-desktop-integration[1558]: See https://forum.snapcraft.io/t/11209 for details.
Jun 30 05:30:05 ty-virtual-machine systemd[836]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Main process exited, code=exited, status=1/FAILURE
Jun 30 05:30:05 ty-virtual-machine systemd[836]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Failed with result 'exit-code'.
Jun 30 05:30:09 ty-virtual-machine systemd[1]: snap.snapd-desktop-integration.hook.configure-3ba1c5b1-c9cc-4ea0-a367-af9b03987bab.scope: Deactivated successfully.
Jun 30 05:30:09 ty-virtual-machine systemd[1]: snap.snapd-desktop-integration.hook.configure-3ba1c5b1-c9cc-4ea0-a367-af9b03987bab.scope: Consumed 2.215s CPU time.
Jun 30 05:30:09 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:30:09 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:30:09 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:30:09 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:30:16 ty-virtual-machine systemd[1]: fprintd.service: Deactivated successfully.
Jun 30 05:30:17 ty-virtual-machine systemd[1]: systemd-localed.service: Deactivated successfully.
Jun 30 05:30:17 ty-virtual-machine systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 30 05:30:34 ty-virtual-machine snap[1542]: fdo.go:203: Cannot remove D-Bus signal matcher: read unix @->/run/user/128/bus: use of closed network connection
Jun 30 05:30:34 ty-virtual-machine snap[1542]: session_agent.go:321: context canceled
Jun 30 05:30:34 ty-virtual-machine snap[1542]: session_agent.go:332: read unix @->/run/user/128/bus: use of closed network connection
Jun 30 05:30:37 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.34' (uid=128 pid=908 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:30:37 ty-virtual-machine systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 30 05:30:37 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 30 05:30:37 ty-virtual-machine systemd[1]: Started Fingerprint Authentication Daemon.
Jun 30 05:30:39 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:30:41 ty-virtual-machine snapd[693]: stateengine.go:149: state ensure error: persistent network error: Get "https://api.snapcraft.io/api/v1/snaps/sections": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 05:30:41 ty-virtual-machine systemd[1]: Finished Wait until snapd is fully seeded.
Jun 30 05:30:41 ty-virtual-machine systemd[1]: Condition check resulted in Auto import assertions from block devices being skipped.
Jun 30 05:30:41 ty-virtual-machine systemd[1]: Reached target Multi-User System.
Jun 30 05:30:41 ty-virtual-machine systemd[1]: Reached target Graphical Interface.
Jun 30 05:30:41 ty-virtual-machine systemd[1]: Starting Record Runlevel Change in UTMP...
Jun 30 05:30:41 ty-virtual-machine systemd[1]: systemd-update-utmp-runlevel.service: Deactivated successfully.
Jun 30 05:30:41 ty-virtual-machine systemd[1]: Finished Record Runlevel Change in UTMP.
Jun 30 05:30:41 ty-virtual-machine systemd[1]: Startup finished in 4.372s (kernel) + 1min 21.692s (userspace) = 1min 26.064s.
Jun 30 05:30:44 ty-virtual-machine geoclue[1067]: Service not used for 60 seconds. Shutting down..
Jun 30 05:30:44 ty-virtual-machine systemd[1]: geoclue.service: Deactivated successfully.
Jun 30 05:30:49 ty-virtual-machine systemd[1]: Created slice User Slice of UID 1000.
Jun 30 05:30:49 ty-virtual-machine systemd[1]: Starting User Runtime Directory /run/user/1000...
Jun 30 05:30:49 ty-virtual-machine systemd[1]: Finished User Runtime Directory /run/user/1000.
Jun 30 05:30:49 ty-virtual-machine systemd[1]: Starting User Manager for UID 1000...
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Queued start job for default target Main User Target.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Created slice User Application Slice.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Created slice User Background Tasks Slice.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Created slice User Core Session Slice.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Started Pending report trigger for Ubuntu Report.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Reached target Paths.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Reached target Timers.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Starting D-Bus User Message Bus Socket...
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on GnuPG network certificate management daemon.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on GnuPG cryptographic agent and passphrase cache.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on PipeWire Multimedia System Socket.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on debconf communication socket.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on Sound System.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on REST API socket for snapd user session agent.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on Speech Dispatcher Socket.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Listening on D-Bus User Message Bus Socket.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Reached target Sockets.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Reached target Basic System.
Jun 30 05:30:49 ty-virtual-machine systemd[1]: Started User Manager for UID 1000.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Started PipeWire Multimedia Service.
Jun 30 05:30:49 ty-virtual-machine systemd[1]: Started Session 2 of User ty.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Started PipeWire Media Session Manager.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Starting Sound Service...
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Started Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Starting Tracker metadata extractor...
Jun 30 05:30:49 ty-virtual-machine rtkit-daemon[856]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:30:49 ty-virtual-machine rtkit-daemon[856]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:30:49 ty-virtual-machine systemd[1668]: Started D-Bus User Message Bus.
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] AppArmor D-Bus mediation is enabled
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.1' (uid=1000 pid=1679 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting Virtual filesystem service...
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Started Virtual filesystem service.
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.freedesktop.portal.Documents' unit='xdg-document-portal.service' requested by ':1.3' (uid=1000 pid=1678 comm="/usr/bin/snap run snapd-desktop-integration " label="unconfined")
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting flatpak document portal service...
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.freedesktop.impl.portal.PermissionStore' unit='xdg-permission-store.service' requested by ':1.5' (uid=1000 pid=1716 comm="/usr/libexec/xdg-document-portal " label="unconfined")
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting sandboxed app permission store...
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Started sandboxed app permission store.
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.portal.Documents'
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Started flatpak document portal service.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 1687 of process 1676 owned by '1000' RT at priority 20.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Supervising 7 threads of 4 processes of 2 users.
Jun 30 05:30:50 ty-virtual-machine kernel: [   94.420855] rfkill: input handler enabled
Jun 30 05:30:50 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.1' (uid=1000 pid=1679 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 1675 of process 1675 owned by '1000' high priority at nice level -11.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Supervising 8 threads of 5 processes of 2 users.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting Tracker file system data miner...
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Created slice Slice /app/gnome-session-manager.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Started Path trigger for Apport crash notifications.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Started Path trigger for new release of Ubuntu notifications.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Reached target GNOME Wayland Session.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Reached target GNOME Shell.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting GNOME Initial Setup Copy Worker...
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting Start gnome-keyring as SSH agent...
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting Start gnome-keyring for the Secrets Service, and PKCS #11...
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting Monitor Session leader for GNOME Session...
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting Session Migration...
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Starting Rewrite dynamic launcher portal entries...
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Started Monitor Session leader for GNOME Session.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Finished GNOME Initial Setup Copy Worker.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Finished Start gnome-keyring for the Secrets Service, and PKCS #11.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Finished Rewrite dynamic launcher portal entries.
Jun 30 05:30:50 ty-virtual-machine sh[1861]: dbus-update-activation-environment: setting SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:30:50 ty-virtual-machine sh[1861]: dbus-update-activation-environment: setting SSH_AGENT_LAUNCHER=gnome-keyring
Jun 30 05:30:50 ty-virtual-machine sh[1829]: /bin/sh: 1: initctl: not found
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Finished Start gnome-keyring as SSH agent.
Jun 30 05:30:50 ty-virtual-machine systemd[1668]: Started OpenSSH Agent.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 1677 of process 1677 owned by '1000' high priority at nice level -11.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Supervising 9 threads of 6 processes of 2 users.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: message repeated 2 times: [ Supervising 9 threads of 6 processes of 2 users.]
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 1877 of process 1675 owned by '1000' RT at priority 20.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Supervising 10 threads of 6 processes of 2 users.
Jun 30 05:30:50 ty-virtual-machine pulseaudio[1677]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Supervising 10 threads of 6 processes of 2 users.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 1889 of process 1677 owned by '1000' RT at priority 5.
Jun 30 05:30:50 ty-virtual-machine rtkit-daemon[856]: Supervising 11 threads of 6 processes of 2 users.
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: ALSA woke us up to write new data to the device, but there was actually nothing to write.
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: Most likely this is a bug in the ALSA driver 'snd_ens1371'. Please report this issue to the ALSA developers.
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: We were woken up with POLLOUT set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 30 05:30:51 ty-virtual-machine rtkit-daemon[856]: Supervising 11 threads of 6 processes of 2 users.
Jun 30 05:30:51 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 1903 of process 1677 owned by '1000' RT at priority 5.
Jun 30 05:30:51 ty-virtual-machine rtkit-daemon[856]: Supervising 12 threads of 6 processes of 2 users.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &DOCUMENTS. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &MUSIC. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &PICTURES. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &VIDEOS. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &DOWNLOAD. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &DOCUMENTS. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &MUSIC. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &PICTURES. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine tracker-miner-f[1802]: Unable to get XDG user directory path for special directory &VIDEOS. Ignoring this location.
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.84' (uid=1000 pid=1677 comm="/usr/bin/pulseaudio --daemonize=no --log-target=jo" label="unconfined")
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: Failed to open cookie file '/home/ty/.config/pulse/cookie': No such file or directory
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: Failed to load authentication key '/home/ty/.config/pulse/cookie': No such file or directory
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: Failed to open cookie file '/home/ty/.pulse-cookie': No such file or directory
Jun 30 05:30:51 ty-virtual-machine pulseaudio[1677]: Failed to load authentication key '/home/ty/.pulse-cookie': No such file or directory
Jun 30 05:30:51 ty-virtual-machine systemd[1]: Condition check resulted in Bluetooth service being skipped.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started Sound Service.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Finished Session Migration.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Reached target Session services which should run early before the graphical session is brought up.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Reached target Tasks to be run before GNOME Session starts.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting GNOME Session Manager (session: ubuntu)...
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dpkcs11-1952.scope: Couldn't move process 1952 to requested cgroup '/user.slice/user-1000.slice/user@1000.service/app.slice/app-gnome-gnome\x2dkeyring\x2dpkcs11-1952.scope': No such process
Jun 30 05:30:51 ty-virtual-machine gnome-keyring-pkcs11.desktop[1960]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:30:51 ty-virtual-machine gnome-keyring-secrets.desktop[1959]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:30:51 ty-virtual-machine gnome-keyring-ssh.desktop[1961]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dpkcs11-1952.scope: Failed to add PIDs to scope's control group: No such process
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dpkcs11-1952.scope: Failed with result 'resources'.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Failed to start Application launched by gnome-session-binary.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dsecrets-1955.scope: Couldn't move process 1955 to requested cgroup '/user.slice/user-1000.slice/user@1000.service/app.slice/app-gnome-gnome\x2dkeyring\x2dsecrets-1955.scope': No such process
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dsecrets-1955.scope: Failed to add PIDs to scope's control group: No such process
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dsecrets-1955.scope: Failed with result 'resources'.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Failed to start Application launched by gnome-session-binary.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dssh-1954.scope: Couldn't move process 1954 to requested cgroup '/user.slice/user-1000.slice/user@1000.service/app.slice/app-gnome-gnome\x2dkeyring\x2dssh-1954.scope': No such process
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dssh-1954.scope: Failed to add PIDs to scope's control group: No such process
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: app-gnome-gnome\x2dkeyring\x2dssh-1954.scope: Failed with result 'resources'.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Failed to start Application launched by gnome-session-binary.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started GNOME Session Manager (session: ubuntu).
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Reached target GNOME Session Manager is ready.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting GNOME Shell on Wayland...
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting GNOME Shell on X11...
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 1.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Stopped GNOME Shell on X11.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting GNOME Shell on X11...
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 2.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Stopped GNOME Shell on X11.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting GNOME Shell on X11...
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started Application launched by gnome-session-binary.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started Application launched by gnome-session-binary.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 3.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Stopped GNOME Shell on X11.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Start request repeated too quickly.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started GNOME Shell on X11.
Jun 30 05:30:51 ty-virtual-machine gnome-shell[1965]: Running GNOME Shell (using mutter 42.9) as a Wayland display server
Jun 30 05:30:51 ty-virtual-machine gnome-shell[1965]: Added device '/dev/dri/card0' (vmwgfx) using non-atomic mode setting.
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gtk.vfs.UDisks2VolumeMonitor' unit='gvfs-udisks2-volume-monitor.service' requested by ':1.21' (uid=1000 pid=1802 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting Virtual filesystem service - disk device monitor...
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gtk.vfs.UDisks2VolumeMonitor'
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started Virtual filesystem service - disk device monitor.
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gtk.vfs.AfcVolumeMonitor' unit='gvfs-afc-volume-monitor.service' requested by ':1.21' (uid=1000 pid=1802 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:30:51 ty-virtual-machine gnome-shell[1965]: Created gbm renderer for '/dev/dri/card0'
Jun 30 05:30:51 ty-virtual-machine gnome-shell[1965]: Boot VGA GPU /dev/dri/card0 selected as primary
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting Virtual filesystem service - Apple File Conduit monitor...
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gtk.vfs.AfcVolumeMonitor'
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started Virtual filesystem service - Apple File Conduit monitor.
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gtk.vfs.MTPVolumeMonitor' unit='gvfs-mtp-volume-monitor.service' requested by ':1.21' (uid=1000 pid=1802 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting Virtual filesystem service - Media Transfer Protocol monitor...
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gtk.vfs.MTPVolumeMonitor'
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started Virtual filesystem service - Media Transfer Protocol monitor.
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gtk.vfs.GPhoto2VolumeMonitor' unit='gvfs-gphoto2-volume-monitor.service' requested by ':1.21' (uid=1000 pid=1802 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting Virtual filesystem service - digital camera monitor...
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gtk.vfs.GPhoto2VolumeMonitor'
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Started Virtual filesystem service - digital camera monitor.
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gtk.vfs.GoaVolumeMonitor' unit='gvfs-goa-volume-monitor.service' requested by ':1.21' (uid=1000 pid=1802 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:30:51 ty-virtual-machine systemd[1668]: Starting Virtual filesystem service - GNOME Online Accounts monitor...
Jun 30 05:30:51 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.gnome.OnlineAccounts' requested by ':1.39' (uid=1000 pid=2003 comm="/usr/libexec/gvfs-goa-volume-monitor " label="unconfined")
Jun 30 05:30:52 ty-virtual-machine snapd-desktop-i[2013]: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Jun 30 05:30:52 ty-virtual-machine snapd-desktop-i[2013]: Failed to do gtk init. Waiting for a new session with desktop capabilities.
Jun 30 05:30:52 ty-virtual-machine snapd-desktop-i[2013]: Checking session /org/freedesktop/login1/session/_32...
Jun 30 05:30:52 ty-virtual-machine snapd-desktop-i[2013]: Is a desktop session! Forcing a reload.
Jun 30 05:30:52 ty-virtual-machine snapd-desktop-i[2013]: Checking session /org/freedesktop/login1/session/c1...
Jun 30 05:30:52 ty-virtual-machine goa-daemon[2007]: goa-daemon version 3.44.0 starting
Jun 30 05:30:52 ty-virtual-machine snapd-desktop-i[2013]: Loop exited. Forcing reload.
Jun 30 05:30:52 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.gnome.Identity' requested by ':1.41' (uid=1000 pid=2007 comm="/usr/libexec/goa-daemon " label="unconfined")
Jun 30 05:30:52 ty-virtual-machine systemd[1668]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Consumed 1.307s CPU time.
Jun 30 05:30:52 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.OnlineAccounts'
Jun 30 05:30:52 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gtk.vfs.GoaVolumeMonitor'
Jun 30 05:30:52 ty-virtual-machine systemd[1668]: Started Virtual filesystem service - GNOME Online Accounts monitor.
Jun 30 05:30:52 ty-virtual-machine gnome-shell[1965]: Using public X11 display :0, (using :1 for managed services)
Jun 30 05:30:52 ty-virtual-machine gnome-shell[1965]: Using Wayland display name 'wayland-0'
Jun 30 05:30:52 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.Identity'
Jun 30 05:30:52 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.Tracker3.Miner.Files'
Jun 30 05:30:52 ty-virtual-machine systemd[1668]: Started Tracker file system data miner.
Jun 30 05:30:52 ty-virtual-machine systemd[1668]: Started Tracker metadata extractor.
Jun 30 05:30:52 ty-virtual-machine systemd[1668]: Reached target Main User Target.
Jun 30 05:30:52 ty-virtual-machine gnome-shell[1965]: Unset XDG_SESSION_ID, getCurrentSessionProxy() called outside a user session. Asking logind directly.
Jun 30 05:30:52 ty-virtual-machine gnome-shell[1965]: Will monitor session 2
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.gnome.Shell.CalendarServer' requested by ':1.34' (uid=1000 pid=1965 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gnome.evolution.dataserver.Sources5' unit='evolution-source-registry.service' requested by ':1.43' (uid=1000 pid=2033 comm="/usr/libexec/gnome-shell-calendar-server " label="unconfined")
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Starting Evolution source registry...
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='ca.desrt.dconf' unit='dconf.service' requested by ':1.44' (uid=1000 pid=2039 comm="/usr/libexec/evolution-source-registry " label="unconfined")
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Starting User preferences database...
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'ca.desrt.dconf'
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Started User preferences database.
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.GeoClue2' unit='geoclue.service' requested by ':1.86' (uid=1000 pid=1965 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:30:53 ty-virtual-machine systemd[1]: Starting Location Lookup Service...
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.evolution.dataserver.Sources5'
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Started Evolution source registry.
Jun 30 05:30:53 ty-virtual-machine gnome-shell[1965]: Telepathy is not available, chat integration will be disabled.
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gnome.evolution.dataserver.Calendar8' unit='evolution-calendar-factory.service' requested by ':1.43' (uid=1000 pid=2033 comm="/usr/libexec/gnome-shell-calendar-server " label="unconfined")
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.Shell.CalendarServer'
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Starting Evolution calendar service...
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.GeoClue2'
Jun 30 05:30:53 ty-virtual-machine systemd[1]: Started Location Lookup Service.
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.evolution.dataserver.Calendar8'
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Started Evolution calendar service.
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gnome.evolution.dataserver.AddressBook10' unit='evolution-addressbook-factory.service' requested by ':1.46' (uid=1000 pid=2051 comm="/usr/libexec/evolution-calendar-factory " label="unconfined")
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Starting Evolution address book service...
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.evolution.dataserver.AddressBook10'
Jun 30 05:30:53 ty-virtual-machine systemd[1668]: Started Evolution address book service.
Jun 30 05:30:53 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.freedesktop.FileManager1' requested by ':1.34' (uid=1000 pid=1965 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:30:54 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.gnome.Shell.Notifications' requested by ':1.34' (uid=1000 pid=1965 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:30:54 ty-virtual-machine at-spi-dbus-bus.desktop[1974]: dbus-daemon[1974]: Activating service name='org.a11y.atspi.Registry' requested by ':1.0' (uid=1000 pid=1965 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:30:54 ty-virtual-machine at-spi-dbus-bus.desktop[1974]: dbus-daemon[1974]: Successfully activated service 'org.a11y.atspi.Registry'
Jun 30 05:30:54 ty-virtual-machine at-spi-dbus-bus.desktop[2091]: SpiRegistry daemon is running with well-known name - org.a11y.atspi.Registry
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME Shell on Wayland.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Scheduled restart job, restart counter is at 1.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME Session is initialized.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: GNOME session X11 services is inactive.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Dependency failed for GNOME XSettings service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: org.gnome.SettingsDaemon.XSettings.service: Job org.gnome.SettingsDaemon.XSettings.service/start failed with result 'dependency'.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: gnome-session-x11-services-ready.target: Job gnome-session-x11-services-ready.target/verify-active failed with result 'dependency'.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME Session (session: ubuntu).
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME XSettings target.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting Signal initialization done to GNOME Session Manager...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting IBus Daemon for GNOME...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME accessibility service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME color management service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME date & time service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME maintenance of expirable data service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME keyboard configuration service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME keyboard shortcuts service...
Jun 30 05:30:54 ty-virtual-machine udisksd[711]: Mounted /dev/sr0 at /media/ty/CDROM on behalf of uid 1000
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME power management service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME printer notifications service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME RFKill support service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME FreeDesktop screensaver service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME file sharing service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME smartcard service...
Jun 30 05:30:54 ty-virtual-machine spice-vdagent[2115]: vdagent virtio channel /dev/virtio-ports/com.redhat.spice.0 does not exist, exiting
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME sound sample caching service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Starting GNOME Wacom tablet support service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Stopped Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Consumed 1.307s CPU time.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:30:54 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.Shell.Notifications'
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Finished Signal initialization done to GNOME Session Manager.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME accessibility service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME maintenance of expirable data service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME accessibility target.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME maintenance of expirable data target.
Jun 30 05:30:54 ty-virtual-machine NetworkManager[675]: <info>  [1782811854.5317] agent-manager: agent[5e003e75e3bda14f,:1.86/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 30 05:30:54 ty-virtual-machine kernel: [   98.726918] audit: type=1400 audit(1782811854.584:62): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=2161 comm="snap-confine" capability=12  capname="net_admin"
Jun 30 05:30:54 ty-virtual-machine kernel: [   98.727290] audit: type=1400 audit(1782811854.584:63): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=2161 comm="snap-confine" capability=38  capname="perfmon"
Jun 30 05:30:54 ty-virtual-machine gnome-session-binary[1932]: Entering running state
Jun 30 05:30:54 ty-virtual-machine gnome-session[1932]: gnome-session-binary[1932]: GnomeDesktop-WARNING: Could not create transient scope for PID 2115: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 2115 does not exist.
Jun 30 05:30:54 ty-virtual-machine gnome-session-binary[1932]: GnomeDesktop-WARNING: Could not create transient scope for PID 2115: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 2115 does not exist.
Jun 30 05:30:54 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.95' (uid=1000 pid=2134 comm="/usr/libexec/gsd-rfkill " label="unconfined")
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME FreeDesktop screensaver service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME smartcard service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started Application launched by gnome-session-binary.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: app-gnome-im\x2dlaunch-2163.scope: Couldn't move process 2163 to requested cgroup '/user.slice/user-1000.slice/user@1000.service/app.slice/app-gnome-im\x2dlaunch-2163.scope': No such process
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: app-gnome-im\x2dlaunch-2163.scope: Failed to add PIDs to scope's control group: No such process
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: app-gnome-im\x2dlaunch-2163.scope: Failed with result 'resources'.
Jun 30 05:30:54 ty-virtual-machine systemd[1]: Starting Hostname Service...
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Failed to start Application launched by gnome-session-binary.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME FreeDesktop screensaver target.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME smartcard target.
Jun 30 05:30:54 ty-virtual-machine at-spi2-registr[2091]: Failed to register client: GDBus.Error:org.gnome.SessionManager.AlreadyRegistered: Unable to register client
Jun 30 05:30:54 ty-virtual-machine at-spi2-registr[2091]: Unable to register client with session manager
Jun 30 05:30:54 ty-virtual-machine gnome-shell[1965]: Error looking up permission: GDBus.Error:org.freedesktop.portal.Error.NotFound: No entry for geolocation
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME date & time service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME file sharing service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME sound sample caching service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started Application launched by gnome-session-binary.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: message repeated 4 times: [ Started Application launched by gnome-session-binary.]
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME date & time target.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME file sharing target.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME sound sample caching target.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME printer notifications service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME printer notifications target.
Jun 30 05:30:54 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 30 05:30:54 ty-virtual-machine systemd[1]: Started Hostname Service.
Jun 30 05:30:54 ty-virtual-machine kernel: [   99.088388] rfkill: input handler disabled
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Started GNOME RFKill support service.
Jun 30 05:30:54 ty-virtual-machine systemd[1668]: Reached target GNOME RFKill support target.
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.freedesktop.portal.IBus' requested by ':1.72' (uid=1000 pid=2129 comm="/usr/bin/ibus-daemon --panel disable " label="unconfined")
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Started IBus Daemon for GNOME.
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gtk.vfs.Metadata' unit='gvfs-metadata.service' requested by ':1.34' (uid=1000 pid=1965 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Starting Virtual filesystem metadata service...
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gtk.vfs.Metadata'
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Started Virtual filesystem metadata service.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Started GNOME color management service.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target GNOME color management target.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Started GNOME keyboard configuration service.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target GNOME keyboard configuration target.
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.locale1' unit='dbus-org.freedesktop.locale1.service' requested by ':1.105' (uid=1000 pid=2118 comm="/usr/libexec/gsd-keyboard " label="unconfined")
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Started GNOME keyboard shortcuts service.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target GNOME keyboard shortcuts target.
Jun 30 05:30:55 ty-virtual-machine systemd[1]: Starting Locale Service...
Jun 30 05:30:55 ty-virtual-machine snapd-desktop-i[2471]: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Started GNOME power management service.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target GNOME power management target.
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.freedesktop.portal.Desktop' unit='xdg-desktop-portal.service' requested by ':1.85' (uid=1000 pid=2471 comm="/snap/snapd-desktop-integration/83/usr/bin/snapd-d" label="snap.snapd-desktop-integration.snapd-desktop-integration (enforce)")
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Starting Portal service...
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Started GNOME Wacom tablet support service.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target GNOME Wacom tablet support target.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target GNOME Session.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target GNOME Wayland Session (session: ubuntu).
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Reached target Current graphical user session.
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Starting GNOME Initial Setup...
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.freedesktop.impl.portal.desktop.gnome' unit='xdg-desktop-portal-gnome.service' requested by ':1.86' (uid=1000 pid=2480 comm="/usr/libexec/xdg-desktop-portal " label="unconfined")
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.locale1'
Jun 30 05:30:55 ty-virtual-machine systemd[1668]: Starting Portal service (GNOME implementation)...
Jun 30 05:30:55 ty-virtual-machine systemd[1]: Started Locale Service.
Jun 30 05:30:55 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.gnome.ScreenSaver' requested by ':1.68' (uid=1000 pid=2130 comm="/usr/libexec/gsd-power " label="unconfined")
Jun 30 05:30:55 ty-virtual-machine gsd-media-keys[2119]: Failed to grab accelerator for keybinding settings:hibernate
Jun 30 05:30:55 ty-virtual-machine gsd-media-keys[2119]: Failed to grab accelerator for keybinding settings:playback-repeat
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:30:55 ty-virtual-machine gnome-shell[1965]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:30:55 ty-virtual-machine gsd-color[2111]: failed to get edid: unable to get EDID for output
Jun 30 05:30:55 ty-virtual-machine gsd-color[1086]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:30:55 ty-virtual-machine gsd-color[2111]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:30:56 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.ScreenSaver'
Jun 30 05:30:56 ty-virtual-machine pulseaudio[1677]: ALSA woke us up to read new data from the device, but there was actually nothing to read.
Jun 30 05:30:56 ty-virtual-machine pulseaudio[1677]: Most likely this is a bug in the ALSA driver 'snd_ens1371'. Please report this issue to the ALSA developers.
Jun 30 05:30:56 ty-virtual-machine pulseaudio[1677]: We were woken up with POLLIN set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 30 05:30:57 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.impl.portal.desktop.gnome'
Jun 30 05:30:57 ty-virtual-machine systemd[1668]: Started Portal service (GNOME implementation).
Jun 30 05:30:57 ty-virtual-machine gnome-shell[1965]: GNOME Shell started at Tue Jun 30 2026 05:30:53 GMT-0400 (EDT)
Jun 30 05:30:57 ty-virtual-machine gnome-shell[1965]: Registering session with GDM
Jun 30 05:30:57 ty-virtual-machine gdm-launch-environment]: GLib-GObject: g_object_unref: assertion 'G_IS_OBJECT (object)' failed
Jun 30 05:30:57 ty-virtual-machine ibus-daemon[1372]: GChildWatchSource: Exit status of a child process was requested but ECHILD was received by waitpid(). See the documentation of g_child_watch_source_new() for possible causes.
Jun 30 05:30:57 ty-virtual-machine rtkit-daemon[856]: Supervising 12 threads of 6 processes of 2 users.
Jun 30 05:30:57 ty-virtual-machine rtkit-daemon[856]: message repeated 2 times: [ Supervising 12 threads of 6 processes of 2 users.]
Jun 30 05:30:57 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.freedesktop.impl.portal.desktop.gtk' unit='xdg-desktop-portal-gtk.service' requested by ':1.86' (uid=1000 pid=2480 comm="/usr/libexec/xdg-desktop-portal " label="unconfined")
Jun 30 05:30:57 ty-virtual-machine systemd[1668]: Starting Portal service (GTK/GNOME implementation)...
Jun 30 05:30:57 ty-virtual-machine systemd[1]: session-c1.scope: Deactivated successfully.
Jun 30 05:30:57 ty-virtual-machine systemd[1]: session-c1.scope: Consumed 9.921s CPU time.
Jun 30 05:30:57 ty-virtual-machine systemd[836]: pulseaudio.service: Consumed 1.442s CPU time.
Jun 30 05:30:57 ty-virtual-machine gnome-initial-s[2481]: Starting gnome-initial-setup
Jun 30 05:30:57 ty-virtual-machine gnome-initial-s[2481]: Production mode: changes will be saved to disk
Jun 30 05:30:58 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.impl.portal.desktop.gtk'
Jun 30 05:30:58 ty-virtual-machine systemd[1668]: Started Portal service (GTK/GNOME implementation).
Jun 30 05:30:58 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='com.canonical.UbuntuAdvantage' unit='ubuntu-advantage-desktop-daemon.service' requested by ':1.112' (uid=1000 pid=2481 comm="/usr/libexec/gnome-initial-setup --existing-user " label="unconfined")
Jun 30 05:30:58 ty-virtual-machine systemd[1]: Starting Desktop service for Ubuntu Advantage...
Jun 30 05:30:58 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.portal.Desktop'
Jun 30 05:30:58 ty-virtual-machine systemd[1668]: Started Portal service.
Jun 30 05:30:58 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'com.canonical.UbuntuAdvantage'
Jun 30 05:30:58 ty-virtual-machine systemd[1]: Started Desktop service for Ubuntu Advantage.
Jun 30 05:30:58 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.FileManager1'
Jun 30 05:30:58 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.gnome.ArchiveManager1' requested by ':1.92' (uid=1000 pid=2545 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 30 05:30:58 ty-virtual-machine snapd-desktop-i[2471]: New theme: gtk=Yaru icon=Yaru cursor=Yaru, sound=Yaru
Jun 30 05:30:58 ty-virtual-machine snapd-desktop-i[2471]: All available theme snaps installed
Jun 30 05:30:59 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 30 05:30:59 ty-virtual-machine gnome-shell[1965]: DING: Detected async api for thumbnails
Jun 30 05:30:59 ty-virtual-machine gnome-shell[1965]: DING: GNOME nautilus 42.6
Jun 30 05:31:04 ty-virtual-machine gnome-initial-setup[2481]: time="2026-06-30T05:31:04-04:00" level=info msg="no DCD information: couldn't open /var/lib/ubuntu_dist_channel: open /var/lib/ubuntu_dist_channel: no such file or directory"
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2672]: (WW) Option "-listen" for file descriptors is deprecated
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2672]: Please use "-listenfd" instead.
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2672]: (WW) Option "-listen" for file descriptors is deprecated
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2672]: Please use "-listenfd" instead.
Jun 30 05:31:04 ty-virtual-machine systemd[1668]: Reached target GNOME session X11 services.
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2676]: The XKEYBOARD keymap compiler (xkbcomp) reports:
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2676]: > Warning:          Unsupported maximum keycode 708, clipping.
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2676]: >                   X11 cannot support keycodes above 255.
Jun 30 05:31:04 ty-virtual-machine gnome-shell[2676]: Errors from xkbcomp are not fatal to the X server
Jun 30 05:31:04 ty-virtual-machine systemd[1668]: Starting GNOME XSettings service...
Jun 30 05:31:05 ty-virtual-machine systemd[1668]: Started GNOME XSettings service.
Jun 30 05:31:05 ty-virtual-machine systemd[1668]: Reached target GNOME session X11 services.
Jun 30 05:31:05 ty-virtual-machine gnome-shell[1965]: ATK Bridge is disabled but a11y has already been enabled.
Jun 30 05:31:05 ty-virtual-machine gnome-initial-setup[2481]: time="2026-06-30T05:31:05-04:00" level=info msg="no upgrade data found: couldn't open /var/log/upgrade/telemetry: open /var/log/upgrade/telemetry: no such file or directory"
Jun 30 05:31:05 ty-virtual-machine gnome-initial-s[2481]: Failed to send report: data were not delivered successfully to metrics server, saving for a later automated report: couldn't send post http request: Post "https://metrics.ubuntu.com/ubuntu/desktop/22.04": dial tcp: lookup metrics.ubuntu.com: Temporary failure in name resolution
Jun 30 05:31:05 ty-virtual-machine systemd[1668]: Started Ubuntu report sends pending metrics data.
Jun 30 05:31:05 ty-virtual-machine ubuntu-report[2712]: level=error msg="data were not delivered successfully to metrics server, retrying in 30s"
Jun 30 05:31:06 ty-virtual-machine systemd[1668]: Finished GNOME Initial Setup.
Jun 30 05:31:06 ty-virtual-machine systemd[1668]: Startup finished in 17.284s.
Jun 30 05:31:06 ty-virtual-machine systemd[1668]: gnome-initial-setup-first-login.service: Consumed 2.352s CPU time.
Jun 30 05:31:07 ty-virtual-machine systemd[1]: Stopping User Manager for UID 128...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped target Main User Target.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping D-Bus User Message Bus...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping Virtual filesystem service - Apple File Conduit monitor...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping Virtual filesystem service...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping Virtual filesystem service - GNOME Online Accounts monitor...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping Virtual filesystem service - digital camera monitor...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping Virtual filesystem service - Media Transfer Protocol monitor...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping Virtual filesystem service - disk device monitor...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping PipeWire Media Session Manager...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping Tracker file system data miner...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping flatpak document portal service...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping sandboxed app permission store...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped Virtual filesystem service - Media Transfer Protocol monitor.
Jun 30 05:31:07 ty-virtual-machine systemd[1]: run-user-128-gvfs.mount: Deactivated successfully.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped Virtual filesystem service - disk device monitor.
Jun 30 05:31:07 ty-virtual-machine systemd[1]: run-user-128-doc.mount: Deactivated successfully.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped PipeWire Media Session Manager.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped Virtual filesystem service.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped Virtual filesystem service - Apple File Conduit monitor.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped Virtual filesystem service - digital camera monitor.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped Virtual filesystem service - GNOME Online Accounts monitor.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: xdg-permission-store.service: Main process exited, code=exited, status=1/FAILURE
Jun 30 05:31:07 ty-virtual-machine systemd[836]: xdg-permission-store.service: Failed with result 'exit-code'.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped sandboxed app permission store.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped D-Bus User Message Bus.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopping PipeWire Multimedia Service...
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped PipeWire Multimedia Service.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Stopped flatpak document portal service.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: Removed slice User Core Session Slice.
Jun 30 05:31:07 ty-virtual-machine systemd[836]: session.slice: Consumed 1.599s CPU time.
Jun 30 05:31:07 ty-virtual-machine systemd[1]: fprintd.service: Deactivated successfully.
Jun 30 05:31:07 ty-virtual-machine tracker-miner-fs-3[988]: OK
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Stopped Tracker file system data miner.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: tracker-miner-fs-3.service: Consumed 1.721s CPU time.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Removed slice User Background Tasks Slice.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: background.slice: Consumed 2.239s CPU time.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Stopped target Basic System.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Stopped target Paths.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Stopped Pending report trigger for Ubuntu Report.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Stopped target Sockets.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Stopped target Timers.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed D-Bus User Message Bus Socket.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed GnuPG network certificate management daemon.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed GnuPG cryptographic agent and passphrase cache (restricted).
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed GnuPG cryptographic agent (ssh-agent emulation).
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed GnuPG cryptographic agent and passphrase cache.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed PipeWire Multimedia System Socket.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed debconf communication socket.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed Sound System.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed REST API socket for snapd user session agent.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Closed Speech Dispatcher Socket.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Removed slice User Application Slice.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: app.slice: Consumed 1.265s CPU time.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Reached target Shutdown.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Finished Exit the Session.
Jun 30 05:31:08 ty-virtual-machine systemd[836]: Reached target Exit the Session.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: user@128.service: Deactivated successfully.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: Stopped User Manager for UID 128.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: user@128.service: Consumed 5.643s CPU time.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: Stopping User Runtime Directory /run/user/128...
Jun 30 05:31:08 ty-virtual-machine systemd[1]: run-user-128.mount: Deactivated successfully.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: user-runtime-dir@128.service: Deactivated successfully.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: Stopped User Runtime Directory /run/user/128.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: Removed slice User Slice of UID 128.
Jun 30 05:31:08 ty-virtual-machine systemd[1]: user-128.slice: Consumed 15.596s CPU time.
Jun 30 05:31:08 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.21' (uid=1000 pid=1802 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:31:08 ty-virtual-machine systemd[1668]: Starting Tracker metadata extractor...
Jun 30 05:31:08 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.freedesktop.Tracker3.Miner.Extract'
Jun 30 05:31:08 ty-virtual-machine systemd[1668]: Started Tracker metadata extractor.
Jun 30 05:31:08 ty-virtual-machine nautilus[2080]: Could not delete '.meta.isrunning': No such file or directory
Jun 30 05:31:11 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:31:11 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:31:12 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:31:12 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:31:12 ty-virtual-machine systemd[1668]: Started Application launched by gnome-shell.
Jun 30 05:31:16 ty-virtual-machine pulseaudio[1677]: GetManagedObjects() failed: org.freedesktop.DBus.Error.NoReply: Did not receive a reply. Possible causes include: the remote application did not send a reply, the message bus security policy blocked the reply, the reply timeout expired, or the network connection was broken.
Jun 30 05:31:20 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.117' (uid=1000 pid=2766 comm="gnome-control-center " label="unconfined")
Jun 30 05:31:20 ty-virtual-machine systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 30 05:31:20 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 30 05:31:20 ty-virtual-machine systemd[1]: Started Fingerprint Authentication Daemon.
Jun 30 05:31:25 ty-virtual-machine systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 30 05:31:25 ty-virtual-machine systemd[1]: systemd-localed.service: Deactivated successfully.
Jun 30 05:31:35 ty-virtual-machine ubuntu-report[2712]: level=error msg="data were not delivered successfully to metrics server, retrying in 60s"
Jun 30 05:31:42 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.locale1' unit='dbus-org.freedesktop.locale1.service' requested by ':1.117' (uid=1000 pid=2766 comm="gnome-control-center " label="unconfined")
Jun 30 05:31:42 ty-virtual-machine systemd[1]: Starting Locale Service...
Jun 30 05:31:42 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:31:42 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:31:42 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:31:42 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.locale1'
Jun 30 05:31:42 ty-virtual-machine systemd[1]: Started Locale Service.
Jun 30 05:31:42 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:31:42 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:31:49 ty-virtual-machine dbus-daemon[674]: [system] Activating service name='org.debian.apt' requested by ':1.121' (uid=1000 pid=2869 comm="/usr/bin/python3 /usr/bin/gnome-language-selector " label="unconfined") (using servicehelper)
Jun 30 05:31:50 ty-virtual-machine AptDaemon: INFO: Initializing daemon
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: 05:31:50 AptDaemon [INFO]: Initializing daemon
Jun 30 05:31:50 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.debian.apt'
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: /usr/lib/python3/dist-packages/aptdaemon/worker/pkworker.py:35: PyGIWarning: PackageKitGlib was imported without specifying a version first. Use gi.require_version('PackageKitGlib', '1.0') before import to ensure that the right version gets loaded.
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]:   from gi.repository import PackageKitGlib as pk
Jun 30 05:31:50 ty-virtual-machine AptDaemon: INFO: UpdateCache() was called
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: 05:31:50 AptDaemon [INFO]: UpdateCache() was called
Jun 30 05:31:50 ty-virtual-machine AptDaemon.Trans: INFO: Queuing transaction /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: 05:31:50 AptDaemon.Trans [INFO]: Queuing transaction /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:50 ty-virtual-machine AptDaemon.Worker: INFO: Simulating trans: /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: 05:31:50 AptDaemon.Worker [INFO]: Simulating trans: /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:50 ty-virtual-machine AptDaemon.Worker: INFO: Processing transaction /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: 05:31:50 AptDaemon.Worker [INFO]: Processing transaction /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:50 ty-virtual-machine AptDaemon.Worker: WARNING: An additional step to open the cache is required
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: 05:31:50 AptDaemon.Worker [WARNING]: An additional step to open the cache is required
Jun 30 05:31:50 ty-virtual-machine AptDaemon.Worker: INFO: Updating cache
Jun 30 05:31:50 ty-virtual-machine org.debian.apt[3219]: 05:31:50 AptDaemon.Worker [INFO]: Updating cache
Jun 30 05:31:50 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 30 05:31:50 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 30 05:31:50 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 30 05:31:50 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 30 05:31:50 ty-virtual-machine python3[3246]: Unable to parse build date from uname version
Jun 30 05:31:50 ty-virtual-machine systemd[1]: fprintd.service: Deactivated successfully.
Jun 30 05:31:50 ty-virtual-machine python3[3246]: Falling back to using timestamp of kernel changelog
Jun 30 05:31:51 ty-virtual-machine python3[3246]: Error updating the cache: [Errno -3] Temporary failure in name resolution
Jun 30 05:31:51 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 30 05:31:51 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 30 05:31:53 ty-virtual-machine geoclue[2048]: Service not used for 60 seconds. Shutting down..
Jun 30 05:31:53 ty-virtual-machine systemd[1]: geoclue.service: Deactivated successfully.
Jun 30 05:31:54 ty-virtual-machine systemd[1668]: Started Application launched by gnome-session-binary.
Jun 30 05:31:54 ty-virtual-machine systemd[1668]: Started Application launched by gnome-session-binary.
Jun 30 05:31:56 ty-virtual-machine ubuntu-appindicators@ubuntu.com[1965]: unable to update icon for software-update-available
Jun 30 05:31:56 ty-virtual-machine ubuntu-appindicators@ubuntu.com[1965]: unable to update icon for livepatch
Jun 30 05:31:57 ty-virtual-machine AptDaemon.Worker: INFO: Finished transaction /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:57 ty-virtual-machine org.debian.apt[3219]: 05:31:57 AptDaemon.Worker [INFO]: Finished transaction /org/debian/apt/transaction/3f3850657b62417cb4f569e06b142972
Jun 30 05:31:57 ty-virtual-machine gnome-shell[1965]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 30 05:32:12 ty-virtual-machine systemd[1]: systemd-localed.service: Deactivated successfully.
Jun 30 05:32:12 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:32:12 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:32:12 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:32:12 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:32:12 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:32:15 ty-virtual-machine update-notifier.desktop[3285]: WARNING:root:timeout reached, exiting
Jun 30 05:32:15 ty-virtual-machine update-notifier.desktop[3285]: Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings
Jun 30 05:32:35 ty-virtual-machine ubuntu-report[2712]: level=error msg="data were not delivered successfully to metrics server, retrying in 120s"
Jun 30 05:32:42 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:32:42 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:32:42 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:32:42 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:32:42 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:32:54 ty-virtual-machine systemd[1668]: Started Application launched by gnome-session-binary.
Jun 30 05:33:12 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:33:12 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:33:12 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:33:13 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:33:13 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:33:43 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:33:43 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:33:43 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:33:43 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:33:43 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:34:13 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:34:13 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:34:13 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:34:13 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:34:13 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:34:25 ty-virtual-machine systemd[1]: Starting Download data for packages that failed at package install time...
Jun 30 05:34:25 ty-virtual-machine systemd[1]: update-notifier-download.service: Deactivated successfully.
Jun 30 05:34:25 ty-virtual-machine systemd[1]: Finished Download data for packages that failed at package install time.
Jun 30 05:34:35 ty-virtual-machine ubuntu-report[2712]: level=error msg="data were not delivered successfully to metrics server, retrying in 240s"
Jun 30 05:34:38 ty-virtual-machine anacron[669]: Job `cron.daily' started
Jun 30 05:34:38 ty-virtual-machine anacron[3372]: Updated timestamp for job `cron.daily' to 2026-06-30
Jun 30 05:34:39 ty-virtual-machine cracklib: no dictionary update necessary.
Jun 30 05:34:39 ty-virtual-machine anacron[669]: Job `cron.daily' terminated
Jun 30 05:34:43 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:34:43 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:34:43 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:34:43 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:34:43 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:35:13 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:35:13 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:35:13 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:35:13 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:35:13 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:35:43 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:35:44 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:35:44 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:35:44 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:35:44 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:36:14 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:36:14 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:36:14 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:36:14 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:36:14 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:36:43 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating via systemd: service name='org.gnome.Terminal' unit='gnome-terminal-server.service' requested by ':1.120' (uid=1000 pid=3471 comm="/usr/bin/gnome-terminal.real --wait " label="unconfined")
Jun 30 05:36:43 ty-virtual-machine systemd[1668]: Created slice Slice /app/org.gnome.Terminal.
Jun 30 05:36:43 ty-virtual-machine systemd[1668]: Starting GNOME Terminal Server...
Jun 30 05:36:43 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.Terminal'
Jun 30 05:36:43 ty-virtual-machine systemd[1668]: Started GNOME Terminal Server.
Jun 30 05:36:43 ty-virtual-machine systemd[1668]: Started VTE child process 3495 launched by gnome-terminal-server process 3476.
Jun 30 05:36:44 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:36:44 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:36:44 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:36:44 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:36:44 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:37:14 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:37:14 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:37:14 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:37:14 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:37:14 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:37:36 ty-virtual-machine systemd[1668]: Started Application launched by gnome-shell.
Jun 30 05:37:36 ty-virtual-machine systemd[1668]: Started snap.firefox.firefox-605888ca-10cd-4198-8bb9-53e45654e693.scope.
Jun 30 05:37:36 ty-virtual-machine kernel: [  500.665292] audit: type=1400 audit(1782812256.524:64): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=3517 comm="snap-confine" capability=12  capname="net_admin"
Jun 30 05:37:36 ty-virtual-machine kernel: [  500.665299] audit: type=1400 audit(1782812256.524:65): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=3517 comm="snap-confine" capability=38  capname="perfmon"
Jun 30 05:37:37 ty-virtual-machine firefox[3517]: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Jun 30 05:37:38 ty-virtual-machine kernel: [  502.707690] audit: type=1107 audit(1782812258.564:66): pid=674 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.13" pid=3517 label="snap.firefox.firefox" peer_pid=709 peer_label="unconfined"
Jun 30 05:37:38 ty-virtual-machine kernel: [  502.707690]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:37:38 ty-virtual-machine kernel: [  502.708494] audit: type=1107 audit(1782812258.564:67): pid=674 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.135" pid=3517 label="snap.firefox.firefox" peer_pid=3515 peer_label="unconfined"
Jun 30 05:37:38 ty-virtual-machine kernel: [  502.708494]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:37:42 ty-virtual-machine rtkit-daemon[856]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:37:42 ty-virtual-machine rtkit-daemon[856]: message repeated 3 times: [ Supervising 6 threads of 3 processes of 1 users.]
Jun 30 05:37:42 ty-virtual-machine rtkit-daemon[856]: Successfully made thread 3823 of process 3517 owned by '1000' RT at priority 10.
Jun 30 05:37:42 ty-virtual-machine rtkit-daemon[856]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:37:42 ty-virtual-machine rtkit-daemon[856]: message repeated 2 times: [ Supervising 7 threads of 4 processes of 1 users.]
Jun 30 05:37:43 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='io.snapcraft.Settings' requested by ':1.127' (uid=1000 pid=3869 comm="dbus-send --print-reply=literal --session --dest=i" label="snap.firefox.firefox (enforce)")
Jun 30 05:37:43 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'io.snapcraft.Settings'
Jun 30 05:37:43 ty-virtual-machine io.snapcraft.Settings[3872]: userd.go:93: Starting snap userd
Jun 30 05:37:43 ty-virtual-machine rtkit-daemon[856]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:37:43 ty-virtual-machine rtkit-daemon[856]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:37:44 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:37:44 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.69' (uid=0 pid=693 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:37:45 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:37:45 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:37:45 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:37:45 ty-virtual-machine kernel: [  509.278175] audit: type=1107 audit(1782812265.136:68): pid=674 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.142" pid=3517 label="snap.firefox.firefox" peer_pid=4167 peer_label="unconfined"
Jun 30 05:37:45 ty-virtual-machine kernel: [  509.278175]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:37:45 ty-virtual-machine rtkit-daemon[856]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:37:46 ty-virtual-machine rtkit-daemon[856]: message repeated 5 times: [ Supervising 7 threads of 4 processes of 1 users.]
Jun 30 05:37:47 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Activating service name='org.gnome.Nautilus' requested by ':1.34' (uid=1000 pid=1965 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:37:47 ty-virtual-machine dbus-daemon[1693]: [session uid=1000 pid=1693] Successfully activated service 'org.gnome.Nautilus'
Jun 30 05:37:48 ty-virtual-machine dbus-daemon[674]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.146' (uid=1000 pid=4350 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 30 05:37:48 ty-virtual-machine systemd[1]: Starting Hostname Service...
Jun 30 05:37:48 ty-virtual-machine dbus-daemon[674]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 30 05:37:48 ty-virtual-machine systemd[1]: Started Hostname Service.
Jun 30 05:37:48 ty-virtual-machine nautilus[4350]: Called "net usershare info" but it failed: Failed to execute child process “net” (No such file or directory)
Jun 30 05:38:40 ty-virtual-machine systemd-modules-load[351]: Inserted module 'lp'
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] Linux version 6.5.0-18-generic (buildd@lcy02-amd64-070) (x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #18~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Feb  7 11:40:03 UTC 2 (Ubuntu 6.5.0-18.18~22.04.1-generic 6.5.8)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic root=UUID=4a64a517-67dd-4c66-898a-7aec80564857 ro find_preseed=/preseed.cfg auto noprompt priority=critical locale=en_US quiet splash
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] KERNEL supported cpus:
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000]   Intel GenuineIntel
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000]   AMD AuthenticAMD
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000]   Hygon HygonGenuine
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000]   Centaur CentaurHauls
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000]   zhaoxin   Shanghai  
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-provided physical RAM map:
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009e7ff] usable
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x000000000009e800-0x000000000009ffff] reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000000dc000-0x00000000000fffff] reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000bfecffff] usable
Jun 30 05:38:40 ty-virtual-machine systemd-modules-load[351]: Inserted module 'ppdev'
Jun 30 05:38:40 ty-virtual-machine systemd-modules-load[351]: Inserted module 'parport_pc'
Jun 30 05:38:40 ty-virtual-machine systemd-modules-load[351]: Inserted module 'msr'
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Flush Journal to Persistent Storage...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Rule-based Manager for Device Events and Files.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Flush Journal to Persistent Storage.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Coldplug All udev Devices.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Show Plymouth Boot Screen...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Received SIGRTMIN+20 from PID 408 (plymouthd).
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Show Plymouth Boot Screen.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Dispatch Password Requests to Console Directory Watch being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Forward Password Requests to Plymouth Directory Watch.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Local Encrypted Volumes.
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[389]: Using default interface naming scheme 'v249'.
Jun 30 05:38:40 ty-virtual-machine mtp-probe: checking bus 1, device 2: "/sys/devices/pci0000:00/0000:00:11.0/0000:02:00.0/usb1/1-1"
Jun 30 05:38:40 ty-virtual-machine mtp-probe: bus: 1, device: 2 was not an MTP device
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[387]: sda: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda' failed with exit code 1.
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[401]: fd0: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/fd0' failed with exit code 1.
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000bfed0000-0x00000000bfefefff] ACPI data
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000bfeff000-0x00000000bfefffff] ACPI NVS
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000bff00000-0x00000000bfffffff] usable
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000f0000000-0x00000000f7ffffff] reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec0ffff] reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x00000000fffe0000-0x00000000ffffffff] reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000013fffffff] usable
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] NX (Execute Disable) protection: active
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] SMBIOS 2.7 present.
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] DMI: VMware, Inc. VMware Virtual Platform/440BX Desktop Reference Platform, BIOS 6.00 11/12/2020
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] vmware: hypercall mode: 0x02
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] Hypervisor detected: VMware
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[388]: sda3: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda3' failed with exit code 1.
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[401]: sda2: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda2' failed with exit code 1.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Found device VMware_Virtual_S EFI\x20System\x20Partition.
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[387]: sda1: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sda1' failed with exit code 1.
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[386]: sr1: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sr1' failed with exit code 1.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting File System Check on /dev/disk/by-uuid/9E97-3BEC...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started File System Check Daemon to report status.
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[397]: sr0: Process '/usr/bin/unshare -m /usr/bin/snap auto-import --mount=/dev/sr0' failed with exit code 1.
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]: fsck.fat 4.2 (2021-01-31)
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]: There are differences between boot sector and its backup.
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]: This is mostly harmless. Differences: (offset:original/backup)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] vmware: TSC freq read from hypervisor : 2419.202 MHz
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] vmware: Host bus clock speed read from hypervisor : 66000000 Hz
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000000] vmware: using clock offset of 19534564432 ns
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.000047] tsc: Detected 2419.202 MHz processor
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.003633] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.003645] e820: remove [mem 0x000a0000-0x000fffff] usable
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.003680] last_pfn = 0x140000 max_arch_pfn = 0x400000000
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.003746] total RAM covered: 130048M
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.004055] Found optimal setting for mtrr clean up
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.004056]  gran_size: 64K 	chunk_size: 64K 	num_reg: 7  	lose cover RAM: 0G
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.004065] MTRR map: 7 entries (5 fixed + 2 variable; max 21), built from 8 variable MTRRs
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.004071] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.004220] e820: update [mem 0xc0000000-0xffffffff] usable ==> reserved
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]:   65:01/00
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]:   Not automatically fixing this.
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]: Dirty bit is set. Fs was not properly unmounted and some data may be corrupt.
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]:  Automatically removing dirty bit.
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]: *** Filesystem was changed ***
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]: Writing changes.
Jun 30 05:38:40 ty-virtual-machine systemd-fsck[458]: /dev/sda2: 11 files, 1555/131063 clusters
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.004238] last_pfn = 0xc0000 max_arch_pfn = 0x400000000
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.014546] found SMP MP-table at [mem 0x000f6a70-0x000f6a7f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.014608] Using GB pages for direct mapping
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.014611] Incomplete global flushes, disabling PCID
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015051] RAMDISK: [mem 0x2fa09000-0x33cfbfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015067] ACPI: Early table checksum verification disabled
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished File System Check on /dev/disk/by-uuid/9E97-3BEC.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Mounting /boot/efi...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Mounted /boot/efi.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Local File Systems.
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015075] ACPI: RSDP 0x00000000000F6A00 000024 (v02 PTLTD )
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Load AppArmor profiles...
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015084] ACPI: XSDT 0x00000000BFEDC633 00005C (v01 INTEL  440BX    06040000 VMW  01324272)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015095] ACPI: FACP 0x00000000BFEFEE73 0000F4 (v04 INTEL  440BX    06040000 PTL  000F4240)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015105] ACPI: DSDT 0x00000000BFEDD9E8 02148B (v01 PTLTD  Custom   06040000 MSFT 03000001)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015120] ACPI: FACS 0x00000000BFEFFFC0 000040
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015126] ACPI: FACS 0x00000000BFEFFFC0 000040
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015131] ACPI: BOOT 0x00000000BFEDD9C0 000028 (v01 PTLTD  $SBFTBL$ 06040000  LTP 00000001)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015137] ACPI: APIC 0x00000000BFEDD27E 000742 (v01 PTLTD  ? APIC   06040000  LTP 00000000)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015142] ACPI: MCFG 0x00000000BFEDD242 00003C (v01 PTLTD  $PCITBL$ 06040000  LTP 00000001)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015148] ACPI: SRAT 0x00000000BFEDC72F 0008D0 (v02 VMWARE MEMPLUG  06040000 VMW  00000001)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015153] ACPI: HPET 0x00000000BFEDC6F7 000038 (v01 VMWARE VMW HPET 06040000 VMW  00000001)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015158] ACPI: WAET 0x00000000BFEDC6CF 000028 (v01 VMWARE VMW WAET 06040000 VMW  00000001)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015163] ACPI: Reserving FACP table memory at [mem 0xbfefee73-0xbfefef66]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015166] ACPI: Reserving DSDT table memory at [mem 0xbfedd9e8-0xbfefee72]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015168] ACPI: Reserving FACS table memory at [mem 0xbfefffc0-0xbfefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015170] ACPI: Reserving FACS table memory at [mem 0xbfefffc0-0xbfefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015172] ACPI: Reserving BOOT table memory at [mem 0xbfedd9c0-0xbfedd9e7]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015173] ACPI: Reserving APIC table memory at [mem 0xbfedd27e-0xbfedd9bf]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015175] ACPI: Reserving MCFG table memory at [mem 0xbfedd242-0xbfedd27d]
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Set console font and keymap...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Tell Plymouth To Write Out Runtime Data...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Set Up Additional Binary Formats...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Commit a transient machine-id on disk being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Create Volatile Files and Directories...
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015176] ACPI: Reserving SRAT table memory at [mem 0xbfedc72f-0xbfedcffe]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015178] ACPI: Reserving HPET table memory at [mem 0xbfedc6f7-0xbfedc72e]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015179] ACPI: Reserving WAET table memory at [mem 0xbfedc6cf-0xbfedc6f6]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015265] system APIC only can use physical flat
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015268] Setting APIC routing to physical flat.
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015468] SRAT: PXM 0 -> APIC 0x00 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015475] SRAT: PXM 0 -> APIC 0x01 -> Node 0
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Uncomplicated firewall...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Set console font and keymap.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Tell Plymouth To Write Out Runtime Data.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Uncomplicated firewall.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Received SIGRTMIN+20 from PID 408 (plymouthd).
Jun 30 05:38:40 ty-virtual-machine systemd[1]: proc-sys-fs-binfmt_misc.automount: Got automount request for /proc/sys/fs/binfmt_misc, triggered by 485 (systemd-binfmt)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015477] SRAT: PXM 0 -> APIC 0x02 -> Node 0
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Preparation for Network.
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015479] SRAT: PXM 0 -> APIC 0x03 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015480] SRAT: PXM 0 -> APIC 0x04 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015482] SRAT: PXM 0 -> APIC 0x05 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015483] SRAT: PXM 0 -> APIC 0x06 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015485] SRAT: PXM 0 -> APIC 0x07 -> Node 0
Jun 30 05:38:40 ty-virtual-machine apparmor.systemd[478]: Restarting AppArmor
Jun 30 05:38:40 ty-virtual-machine apparmor.systemd[478]: Reloading AppArmor profiles
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Mounting Arbitrary Executable File Formats File System...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Mounted Arbitrary Executable File Formats File System.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Set Up Additional Binary Formats.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Create Volatile Files and Directories.
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015486] SRAT: PXM 0 -> APIC 0x08 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015488] SRAT: PXM 0 -> APIC 0x09 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015489] SRAT: PXM 0 -> APIC 0x0a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015490] SRAT: PXM 0 -> APIC 0x0b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015492] SRAT: PXM 0 -> APIC 0x0c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015493] SRAT: PXM 0 -> APIC 0x0d -> Node 0
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Userspace Out-Of-Memory (OOM) Killer...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Network Name Resolution...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Network Time Synchronization...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Record System Boot/Shutdown in UTMP...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Record System Boot/Shutdown in UTMP.
Jun 30 05:38:40 ty-virtual-machine apparmor.systemd[536]: Skipping profile in /etc/apparmor.d/disable: usr.sbin.rsyslogd
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015495] SRAT: PXM 0 -> APIC 0x0e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015496] SRAT: PXM 0 -> APIC 0x0f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015498] SRAT: PXM 0 -> APIC 0x10 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015500] SRAT: PXM 0 -> APIC 0x11 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015501] SRAT: PXM 0 -> APIC 0x12 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015503] SRAT: PXM 0 -> APIC 0x13 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015504] SRAT: PXM 0 -> APIC 0x14 -> Node 0
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Load AppArmor profiles.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Load AppArmor profiles managed internally by snapd...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Userspace Out-Of-Memory (OOM) Killer.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Network Time Synchronization.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target System Time Set.
Jun 30 05:38:40 ty-virtual-machine systemd-resolved[518]: Positive Trust Anchors:
Jun 30 05:38:40 ty-virtual-machine systemd-resolved[518]: . IN DS 20326 8 2 e06d44b80b8f1d39a95c0b0d7c65d08458e880409bbc683457104237c7f8ec8d
Jun 30 05:38:40 ty-virtual-machine systemd-resolved[518]: Negative trust anchors: home.arpa 10.in-addr.arpa 16.172.in-addr.arpa 17.172.in-addr.arpa 18.172.in-addr.arpa 19.172.in-addr.arpa 20.172.in-addr.arpa 21.172.in-addr.arpa 22.172.in-addr.arpa 23.172.in-addr.arpa 24.172.in-addr.arpa 25.172.in-addr.arpa 26.172.in-addr.arpa 27.172.in-addr.arpa 28.172.in-addr.arpa 29.172.in-addr.arpa 30.172.in-addr.arpa 31.172.in-addr.arpa 168.192.in-addr.arpa d.f.ip6.arpa corp home internal intranet lan local private test
Jun 30 05:38:40 ty-virtual-machine systemd-resolved[518]: Using system hostname 'ty-virtual-machine'.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Network Name Resolution.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Host and Network Name Lookups.
Jun 30 05:38:40 ty-virtual-machine snapd-apparmor[557]: main.go:124: Loading profiles [/var/lib/snapd/apparmor/profiles/snap-confine.snapd.20671 /var/lib/snapd/apparmor/profiles/snap-update-ns.firefox /var/lib/snapd/apparmor/profiles/snap-update-ns.snap-store /var/lib/snapd/apparmor/profiles/snap-update-ns.snapd-desktop-integration /var/lib/snapd/apparmor/profiles/snap.firefox.firefox /var/lib/snapd/apparmor/profiles/snap.firefox.geckodriver /var/lib/snapd/apparmor/profiles/snap.firefox.hook.configure /var/lib/snapd/apparmor/profiles/snap.firefox.hook.connect-plug-host-hunspell /var/lib/snapd/apparmor/profiles/snap.firefox.hook.disconnect-plug-host-hunspell /var/lib/snapd/apparmor/profiles/snap.firefox.hook.post-refresh /var/lib/snapd/apparmor/profiles/snap.snap-store.hook.configure /var/lib/snapd/apparmor/profiles/snap.snap-store.snap-store /var/lib/snapd/apparmor/profiles/snap.snap-store.ubuntu-software /var/lib/snapd/apparmor/profiles/snap.snap-store.ubuntu-software-local-file /var/lib/snapd/apparmor/profiles/snap.snapd-desktop-integration.hook.configure /var/lib/snapd/apparmor/profiles/snap.snapd-desktop-integration.snapd-desktop-integration]
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Load AppArmor profiles managed internally by snapd.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target System Initialization.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started ACPI Events Check.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Process error reports when automatic reporting is enabled (file watch) being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started CUPS Scheduler.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Start whoopsie on modification of the /var/crash directory.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Trigger anacron every hour.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Process error reports when automatic reporting is enabled (timer based) being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Daily apt download activities.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Daily apt upgrade and clean activities.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Daily dpkg database backup timer.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Periodic ext4 Online Metadata Check for All Filesystems.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Discard unused blocks once a week.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Refresh fwupd metadata regularly.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Daily rotation of log files.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Daily man-db regeneration.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Message of the Day.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Timer to automatically fetch and run repair assertions being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Daily Cleanup of Temporary Directories.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Ubuntu Pro Timer for running repeated jobs being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Path Units.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Listening on ACPID Listen Socket.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Unix socket for apport crash forwarding being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Listening on CUPS Scheduler.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Listening on D-Bus System Message Bus Socket.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Socket activation for snappy daemon...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Listening on UUID daemon activation socket.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Listening on Socket activation for snappy daemon.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Socket Units.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Basic System.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Accounts Service...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started ACPI event daemon.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Run anacron jobs.
Jun 30 05:38:40 ty-virtual-machine anacron[714]: Anacron 2.3 started on 2026-06-30
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting LSB: automatic crash report generation...
Jun 30 05:38:40 ty-virtual-machine anacron[714]: Will run job `cron.weekly' in 10 min.
Jun 30 05:38:40 ty-virtual-machine anacron[714]: Will run job `cron.monthly' in 15 min.
Jun 30 05:38:40 ty-virtual-machine anacron[714]: Jobs will be executed sequentially
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Avahi mDNS/DNS-SD Stack...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Regular background program processing daemon.
Jun 30 05:38:40 ty-virtual-machine cron[718]: (CRON) INFO (pidfile fd = 3)
Jun 30 05:38:40 ty-virtual-machine cron[718]: (CRON) INFO (Running @reboot jobs)
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Found user 'avahi' (UID 114) and group 'avahi' (GID 121).
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started D-Bus System Message Bus.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Network Manager...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Save initial kernel messages after boot.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Remove Stale Online ext4 Metadata Check Snapshots...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in getty on tty2-tty6 if dbus and logind are not available being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Login Prompts.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Detect the available GPUs and deal with any system changes...
Jun 30 05:38:40 ty-virtual-machine systemd-udevd[391]: controlC0: Process '/usr/sbin/alsactl -E HOME=/run/alsa -E XDG_RUNTIME_DIR=/run/alsa/runtime restore 0' failed with exit code 2.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Record successful boot for GRUB...
Jun 30 05:38:40 ty-virtual-machine dbus-daemon[719]: dbus[719]: Unknown group "power" in message bus configuration file
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started irqbalance daemon.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Dispatcher daemon for systemd-networkd...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Authorization Manager...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Power Profiles daemon...
Jun 30 05:38:40 ty-virtual-machine dbus-daemon[719]: [system] AppArmor D-Bus mediation is enabled
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting System Logging Service...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Secure Boot updates for DB and DBX being skipped.
Jun 30 05:38:40 ty-virtual-machine acpid: starting up with netlink and the input layer
Jun 30 05:38:40 ty-virtual-machine acpid: 8 rules loaded
Jun 30 05:38:40 ty-virtual-machine acpid: waiting for events: event logging is off
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Userspace listener for prompt events.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Automatically repair incorrect owner/permissions on core devices being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Wait for the Ubuntu Core chooser trigger being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Preparation for Logins.
Jun 30 05:38:40 ty-virtual-machine polkitd[741]: started daemon version 0.105 using authority implementation `local' version `0.105'
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Snap Daemon...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Switcheroo Control Proxy service...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting User Login Management...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Thermal Daemon Service being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Ubuntu Pro reboot cmds being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Disk Manager...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting WPA supplicant...
Jun 30 05:38:40 ty-virtual-machine NetworkManager[721]: <info>  [1782812320.5028] NetworkManager (version 1.36.6) is starting... (for the first time)
Jun 30 05:38:40 ty-virtual-machine NetworkManager[721]: <info>  [1782812320.5030] Read config: /etc/NetworkManager/NetworkManager.conf (lib: 10-dns-resolved.conf, 20-connectivity-ubuntu.conf, no-mac-addr-change.conf) (run: 10-globally-managed-devices.conf) (etc: default-wifi-powersave-on.conf)
Jun 30 05:38:40 ty-virtual-machine NetworkManager[721]: <info>  [1782812320.5329] bus-manager: acquired D-Bus service "org.freedesktop.NetworkManager"
Jun 30 05:38:40 ty-virtual-machine systemd[1]: gpu-manager.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Detect the available GPUs and deal with any system changes.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: e2scrub_reap.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Remove Stale Online ext4 Metadata Check Snapshots.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Successfully dropped root privileges.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: avahi-daemon 0.8 starting up.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Successfully called chroot().
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Successfully dropped remaining capabilities.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: No service file found in /etc/avahi/services.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface lo.IPv6 with address ::1.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: New relevant interface lo.IPv6 for mDNS.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface lo.IPv4 with address 127.0.0.1.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: New relevant interface lo.IPv4 for mDNS.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Network interface enumeration completed.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Registering new address record for ::1 on lo.*.
Jun 30 05:38:40 ty-virtual-machine avahi-daemon[716]: Registering new address record for 127.0.0.1 on lo.IPv4.
Jun 30 05:38:40 ty-virtual-machine NetworkManager[721]: <info>  [1782812320.6161] manager[0x55960a88e040]: monitoring kernel firmware directory '/lib/firmware'.
Jun 30 05:38:40 ty-virtual-machine NetworkManager[721]: <info>  [1782812320.6173] monitoring ifupdown state file '/run/network/ifstate'.
Jun 30 05:38:40 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 05:38:40 ty-virtual-machine rsyslogd: imuxsock: Acquired UNIX socket '/run/systemd/journal/syslog' (fd 3) from systemd.  [v8.2112.0]
Jun 30 05:38:40 ty-virtual-machine rsyslogd: rsyslogd's groupid changed to 111
Jun 30 05:38:40 ty-virtual-machine rsyslogd: rsyslogd's userid changed to 104
Jun 30 05:38:40 ty-virtual-machine rsyslogd: [origin software="rsyslogd" swVersion="8.2112.0" x-pid="747" x-info="https://www.rsyslog.com"] start
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started System Logging Service.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Network Manager.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: grub-common.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Record successful boot for GRUB.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Authorization Manager.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Power Profiles daemon.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Avahi mDNS/DNS-SD Stack.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Switcheroo Control Proxy service.
Jun 30 05:38:40 ty-virtual-machine apport[715]:  * Starting automatic crash report generation: apport
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015506] SRAT: PXM 0 -> APIC 0x15 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015507] SRAT: PXM 0 -> APIC 0x16 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015509] SRAT: PXM 0 -> APIC 0x17 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015510] SRAT: PXM 0 -> APIC 0x18 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015512] SRAT: PXM 0 -> APIC 0x19 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015514] SRAT: PXM 0 -> APIC 0x1a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015515] SRAT: PXM 0 -> APIC 0x1b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015517] SRAT: PXM 0 -> APIC 0x1c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015518] SRAT: PXM 0 -> APIC 0x1d -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015520] SRAT: PXM 0 -> APIC 0x1e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015521] SRAT: PXM 0 -> APIC 0x1f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015523] SRAT: PXM 0 -> APIC 0x20 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015524] SRAT: PXM 0 -> APIC 0x21 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015526] SRAT: PXM 0 -> APIC 0x22 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015527] SRAT: PXM 0 -> APIC 0x23 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015529] SRAT: PXM 0 -> APIC 0x24 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015530] SRAT: PXM 0 -> APIC 0x25 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015532] SRAT: PXM 0 -> APIC 0x26 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015533] SRAT: PXM 0 -> APIC 0x27 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015535] SRAT: PXM 0 -> APIC 0x28 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015536] SRAT: PXM 0 -> APIC 0x29 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015538] SRAT: PXM 0 -> APIC 0x2a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015539] SRAT: PXM 0 -> APIC 0x2b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015540] SRAT: PXM 0 -> APIC 0x2c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015542] SRAT: PXM 0 -> APIC 0x2d -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015543] SRAT: PXM 0 -> APIC 0x2e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015545] SRAT: PXM 0 -> APIC 0x2f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015546] SRAT: PXM 0 -> APIC 0x30 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015548] SRAT: PXM 0 -> APIC 0x31 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015549] SRAT: PXM 0 -> APIC 0x32 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015551] SRAT: PXM 0 -> APIC 0x33 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015552] SRAT: PXM 0 -> APIC 0x34 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015553] SRAT: PXM 0 -> APIC 0x35 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015555] SRAT: PXM 0 -> APIC 0x36 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015556] SRAT: PXM 0 -> APIC 0x37 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015558] SRAT: PXM 0 -> APIC 0x38 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015559] SRAT: PXM 0 -> APIC 0x39 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015561] SRAT: PXM 0 -> APIC 0x3a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015562] SRAT: PXM 0 -> APIC 0x3b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015564] SRAT: PXM 0 -> APIC 0x3c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015565] SRAT: PXM 0 -> APIC 0x3d -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015567] SRAT: PXM 0 -> APIC 0x3e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015568] SRAT: PXM 0 -> APIC 0x3f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015569] SRAT: PXM 0 -> APIC 0x40 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015571] SRAT: PXM 0 -> APIC 0x41 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015572] SRAT: PXM 0 -> APIC 0x42 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015574] SRAT: PXM 0 -> APIC 0x43 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015575] SRAT: PXM 0 -> APIC 0x44 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015577] SRAT: PXM 0 -> APIC 0x45 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015578] SRAT: PXM 0 -> APIC 0x46 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015580] SRAT: PXM 0 -> APIC 0x47 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015581] SRAT: PXM 0 -> APIC 0x48 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015583] SRAT: PXM 0 -> APIC 0x49 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015584] SRAT: PXM 0 -> APIC 0x4a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015586] SRAT: PXM 0 -> APIC 0x4b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015587] SRAT: PXM 0 -> APIC 0x4c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015589] SRAT: PXM 0 -> APIC 0x4d -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015590] SRAT: PXM 0 -> APIC 0x4e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015591] SRAT: PXM 0 -> APIC 0x4f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015593] SRAT: PXM 0 -> APIC 0x50 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015594] SRAT: PXM 0 -> APIC 0x51 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015596] SRAT: PXM 0 -> APIC 0x52 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015597] SRAT: PXM 0 -> APIC 0x53 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015599] SRAT: PXM 0 -> APIC 0x54 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015600] SRAT: PXM 0 -> APIC 0x55 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015602] SRAT: PXM 0 -> APIC 0x56 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015603] SRAT: PXM 0 -> APIC 0x57 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015605] SRAT: PXM 0 -> APIC 0x58 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015606] SRAT: PXM 0 -> APIC 0x59 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015608] SRAT: PXM 0 -> APIC 0x5a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015609] SRAT: PXM 0 -> APIC 0x5b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015611] SRAT: PXM 0 -> APIC 0x5c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015612] SRAT: PXM 0 -> APIC 0x5d -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015614] SRAT: PXM 0 -> APIC 0x5e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015615] SRAT: PXM 0 -> APIC 0x5f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015617] SRAT: PXM 0 -> APIC 0x60 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015618] SRAT: PXM 0 -> APIC 0x61 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015620] SRAT: PXM 0 -> APIC 0x62 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015621] SRAT: PXM 0 -> APIC 0x63 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015623] SRAT: PXM 0 -> APIC 0x64 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015624] SRAT: PXM 0 -> APIC 0x65 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015626] SRAT: PXM 0 -> APIC 0x66 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015627] SRAT: PXM 0 -> APIC 0x67 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015629] SRAT: PXM 0 -> APIC 0x68 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015630] SRAT: PXM 0 -> APIC 0x69 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015632] SRAT: PXM 0 -> APIC 0x6a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015633] SRAT: PXM 0 -> APIC 0x6b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015635] SRAT: PXM 0 -> APIC 0x6c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015636] SRAT: PXM 0 -> APIC 0x6d -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015638] SRAT: PXM 0 -> APIC 0x6e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015639] SRAT: PXM 0 -> APIC 0x6f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015641] SRAT: PXM 0 -> APIC 0x70 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015642] SRAT: PXM 0 -> APIC 0x71 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015644] SRAT: PXM 0 -> APIC 0x72 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015645] SRAT: PXM 0 -> APIC 0x73 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015647] SRAT: PXM 0 -> APIC 0x74 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015648] SRAT: PXM 0 -> APIC 0x75 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015649] SRAT: PXM 0 -> APIC 0x76 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015651] SRAT: PXM 0 -> APIC 0x77 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015652] SRAT: PXM 0 -> APIC 0x78 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015654] SRAT: PXM 0 -> APIC 0x79 -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015655] SRAT: PXM 0 -> APIC 0x7a -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015657] SRAT: PXM 0 -> APIC 0x7b -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015658] SRAT: PXM 0 -> APIC 0x7c -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015660] SRAT: PXM 0 -> APIC 0x7d -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015661] SRAT: PXM 0 -> APIC 0x7e -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015663] SRAT: PXM 0 -> APIC 0x7f -> Node 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015668] ACPI: SRAT: Node 0 PXM 0 [mem 0x00000000-0x0009ffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015672] ACPI: SRAT: Node 0 PXM 0 [mem 0x00100000-0xbfffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015675] ACPI: SRAT: Node 0 PXM 0 [mem 0x100000000-0x13fffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015678] ACPI: SRAT: Node 0 PXM 0 [mem 0x140000000-0x103fffffff] hotplug
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015685] NUMA: Node 0 [mem 0x00000000-0x0009ffff] + [mem 0x00100000-0xbfffffff] -> [mem 0x00000000-0xbfffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015690] NUMA: Node 0 [mem 0x00000000-0xbfffffff] + [mem 0x100000000-0x13fffffff] -> [mem 0x00000000-0x13fffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.015707] NODE_DATA(0) allocated [mem 0x13ffd3000-0x13fffdfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018091] Zone ranges:
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018095]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018101]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018104]   Normal   [mem 0x0000000100000000-0x000000013fffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018107]   Device   empty
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018110] Movable zone start for each node
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018113] Early memory node ranges
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018114]   node   0: [mem 0x0000000000001000-0x000000000009dfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018117]   node   0: [mem 0x0000000000100000-0x00000000bfecffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018120]   node   0: [mem 0x00000000bff00000-0x00000000bfffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018122]   node   0: [mem 0x0000000100000000-0x000000013fffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018125] Initmem setup node 0 [mem 0x0000000000001000-0x000000013fffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018306] On node 0, zone DMA: 1 pages in unavailable ranges
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.020656] On node 0, zone DMA: 98 pages in unavailable ranges
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.488836] On node 0, zone DMA32: 48 pages in unavailable ranges
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649542] ACPI: PM-Timer IO Port: 0x1008
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649560] system APIC only can use physical flat
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649584] ACPI: LAPIC_NMI (acpi_id[0x00] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649588] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649590] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649592] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649593] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649595] ACPI: LAPIC_NMI (acpi_id[0x05] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649596] ACPI: LAPIC_NMI (acpi_id[0x06] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649598] ACPI: LAPIC_NMI (acpi_id[0x07] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649599] ACPI: LAPIC_NMI (acpi_id[0x08] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649600] ACPI: LAPIC_NMI (acpi_id[0x09] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649602] ACPI: LAPIC_NMI (acpi_id[0x0a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649603] ACPI: LAPIC_NMI (acpi_id[0x0b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649605] ACPI: LAPIC_NMI (acpi_id[0x0c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649606] ACPI: LAPIC_NMI (acpi_id[0x0d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649608] ACPI: LAPIC_NMI (acpi_id[0x0e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649609] ACPI: LAPIC_NMI (acpi_id[0x0f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649610] ACPI: LAPIC_NMI (acpi_id[0x10] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649612] ACPI: LAPIC_NMI (acpi_id[0x11] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649614] ACPI: LAPIC_NMI (acpi_id[0x12] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649615] ACPI: LAPIC_NMI (acpi_id[0x13] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649617] ACPI: LAPIC_NMI (acpi_id[0x14] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649618] ACPI: LAPIC_NMI (acpi_id[0x15] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649620] ACPI: LAPIC_NMI (acpi_id[0x16] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649621] ACPI: LAPIC_NMI (acpi_id[0x17] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649623] ACPI: LAPIC_NMI (acpi_id[0x18] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649624] ACPI: LAPIC_NMI (acpi_id[0x19] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649625] ACPI: LAPIC_NMI (acpi_id[0x1a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649627] ACPI: LAPIC_NMI (acpi_id[0x1b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649628] ACPI: LAPIC_NMI (acpi_id[0x1c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649630] ACPI: LAPIC_NMI (acpi_id[0x1d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649631] ACPI: LAPIC_NMI (acpi_id[0x1e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649633] ACPI: LAPIC_NMI (acpi_id[0x1f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649634] ACPI: LAPIC_NMI (acpi_id[0x20] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649635] ACPI: LAPIC_NMI (acpi_id[0x21] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649637] ACPI: LAPIC_NMI (acpi_id[0x22] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649638] ACPI: LAPIC_NMI (acpi_id[0x23] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649640] ACPI: LAPIC_NMI (acpi_id[0x24] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649641] ACPI: LAPIC_NMI (acpi_id[0x25] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649643] ACPI: LAPIC_NMI (acpi_id[0x26] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649644] ACPI: LAPIC_NMI (acpi_id[0x27] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649645] ACPI: LAPIC_NMI (acpi_id[0x28] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649647] ACPI: LAPIC_NMI (acpi_id[0x29] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649648] ACPI: LAPIC_NMI (acpi_id[0x2a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649650] ACPI: LAPIC_NMI (acpi_id[0x2b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649651] ACPI: LAPIC_NMI (acpi_id[0x2c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649653] ACPI: LAPIC_NMI (acpi_id[0x2d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649654] ACPI: LAPIC_NMI (acpi_id[0x2e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649655] ACPI: LAPIC_NMI (acpi_id[0x2f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649657] ACPI: LAPIC_NMI (acpi_id[0x30] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649658] ACPI: LAPIC_NMI (acpi_id[0x31] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649660] ACPI: LAPIC_NMI (acpi_id[0x32] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649661] ACPI: LAPIC_NMI (acpi_id[0x33] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649663] ACPI: LAPIC_NMI (acpi_id[0x34] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649664] ACPI: LAPIC_NMI (acpi_id[0x35] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649666] ACPI: LAPIC_NMI (acpi_id[0x36] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649667] ACPI: LAPIC_NMI (acpi_id[0x37] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649668] ACPI: LAPIC_NMI (acpi_id[0x38] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649670] ACPI: LAPIC_NMI (acpi_id[0x39] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649671] ACPI: LAPIC_NMI (acpi_id[0x3a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649673] ACPI: LAPIC_NMI (acpi_id[0x3b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649674] ACPI: LAPIC_NMI (acpi_id[0x3c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649676] ACPI: LAPIC_NMI (acpi_id[0x3d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649677] ACPI: LAPIC_NMI (acpi_id[0x3e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649678] ACPI: LAPIC_NMI (acpi_id[0x3f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649680] ACPI: LAPIC_NMI (acpi_id[0x40] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649681] ACPI: LAPIC_NMI (acpi_id[0x41] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649683] ACPI: LAPIC_NMI (acpi_id[0x42] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649684] ACPI: LAPIC_NMI (acpi_id[0x43] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649686] ACPI: LAPIC_NMI (acpi_id[0x44] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649687] ACPI: LAPIC_NMI (acpi_id[0x45] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649688] ACPI: LAPIC_NMI (acpi_id[0x46] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649690] ACPI: LAPIC_NMI (acpi_id[0x47] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649691] ACPI: LAPIC_NMI (acpi_id[0x48] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649693] ACPI: LAPIC_NMI (acpi_id[0x49] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649694] ACPI: LAPIC_NMI (acpi_id[0x4a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649696] ACPI: LAPIC_NMI (acpi_id[0x4b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649697] ACPI: LAPIC_NMI (acpi_id[0x4c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649698] ACPI: LAPIC_NMI (acpi_id[0x4d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649700] ACPI: LAPIC_NMI (acpi_id[0x4e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649701] ACPI: LAPIC_NMI (acpi_id[0x4f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649703] ACPI: LAPIC_NMI (acpi_id[0x50] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649704] ACPI: LAPIC_NMI (acpi_id[0x51] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649706] ACPI: LAPIC_NMI (acpi_id[0x52] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649707] ACPI: LAPIC_NMI (acpi_id[0x53] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649708] ACPI: LAPIC_NMI (acpi_id[0x54] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649710] ACPI: LAPIC_NMI (acpi_id[0x55] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649711] ACPI: LAPIC_NMI (acpi_id[0x56] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649713] ACPI: LAPIC_NMI (acpi_id[0x57] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649714] ACPI: LAPIC_NMI (acpi_id[0x58] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649716] ACPI: LAPIC_NMI (acpi_id[0x59] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649717] ACPI: LAPIC_NMI (acpi_id[0x5a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649718] ACPI: LAPIC_NMI (acpi_id[0x5b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649720] ACPI: LAPIC_NMI (acpi_id[0x5c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649721] ACPI: LAPIC_NMI (acpi_id[0x5d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649723] ACPI: LAPIC_NMI (acpi_id[0x5e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649724] ACPI: LAPIC_NMI (acpi_id[0x5f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649726] ACPI: LAPIC_NMI (acpi_id[0x60] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649727] ACPI: LAPIC_NMI (acpi_id[0x61] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649729] ACPI: LAPIC_NMI (acpi_id[0x62] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649730] ACPI: LAPIC_NMI (acpi_id[0x63] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649731] ACPI: LAPIC_NMI (acpi_id[0x64] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649733] ACPI: LAPIC_NMI (acpi_id[0x65] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649734] ACPI: LAPIC_NMI (acpi_id[0x66] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649736] ACPI: LAPIC_NMI (acpi_id[0x67] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649737] ACPI: LAPIC_NMI (acpi_id[0x68] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649739] ACPI: LAPIC_NMI (acpi_id[0x69] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649740] ACPI: LAPIC_NMI (acpi_id[0x6a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649741] ACPI: LAPIC_NMI (acpi_id[0x6b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649743] ACPI: LAPIC_NMI (acpi_id[0x6c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649744] ACPI: LAPIC_NMI (acpi_id[0x6d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649746] ACPI: LAPIC_NMI (acpi_id[0x6e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649747] ACPI: LAPIC_NMI (acpi_id[0x6f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649749] ACPI: LAPIC_NMI (acpi_id[0x70] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649750] ACPI: LAPIC_NMI (acpi_id[0x71] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649751] ACPI: LAPIC_NMI (acpi_id[0x72] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649753] ACPI: LAPIC_NMI (acpi_id[0x73] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649754] ACPI: LAPIC_NMI (acpi_id[0x74] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649756] ACPI: LAPIC_NMI (acpi_id[0x75] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649757] ACPI: LAPIC_NMI (acpi_id[0x76] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649759] ACPI: LAPIC_NMI (acpi_id[0x77] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649760] ACPI: LAPIC_NMI (acpi_id[0x78] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649761] ACPI: LAPIC_NMI (acpi_id[0x79] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649763] ACPI: LAPIC_NMI (acpi_id[0x7a] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649764] ACPI: LAPIC_NMI (acpi_id[0x7b] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649766] ACPI: LAPIC_NMI (acpi_id[0x7c] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649767] ACPI: LAPIC_NMI (acpi_id[0x7d] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649769] ACPI: LAPIC_NMI (acpi_id[0x7e] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649770] ACPI: LAPIC_NMI (acpi_id[0x7f] high edge lint[0x1])
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649870] IOAPIC[0]: apic_id 128, version 32, address 0xfec00000, GSI 0-23
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649880] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 high edge)
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649894] ACPI: Using ACPI (MADT) for SMP configuration information
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649897] ACPI: HPET id: 0x8086af01 base: 0xfed00000
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649904] TSC deadline timer available
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649907] smpboot: Allowing 128 CPUs, 124 hotplug CPUs
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649930] PM: hibernation: Registered nosave memory: [mem 0x00000000-0x00000fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649933] PM: hibernation: Registered nosave memory: [mem 0x0009e000-0x0009efff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649935] PM: hibernation: Registered nosave memory: [mem 0x0009f000-0x0009ffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649937] PM: hibernation: Registered nosave memory: [mem 0x000a0000-0x000dbfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649938] PM: hibernation: Registered nosave memory: [mem 0x000dc000-0x000fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649940] PM: hibernation: Registered nosave memory: [mem 0xbfed0000-0xbfefefff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.649942] PM: hibernation: Registered nosave memory: [mem 0xbfeff000-0xbfefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650010] PM: hibernation: Registered nosave memory: [mem 0xc0000000-0xefffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650013] PM: hibernation: Registered nosave memory: [mem 0xf0000000-0xf7ffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650015] PM: hibernation: Registered nosave memory: [mem 0xf8000000-0xfebfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650016] PM: hibernation: Registered nosave memory: [mem 0xfec00000-0xfec0ffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650017] PM: hibernation: Registered nosave memory: [mem 0xfec10000-0xfedfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650019] PM: hibernation: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650020] PM: hibernation: Registered nosave memory: [mem 0xfee01000-0xfffdffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650021] PM: hibernation: Registered nosave memory: [mem 0xfffe0000-0xffffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650024] [mem 0xc0000000-0xefffffff] available for PCI devices
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650027] Booting paravirtualized kernel on VMware hypervisor
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650031] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.650154] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:128 nr_cpu_ids:128 nr_node_ids:1
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963187] percpu: Embedded 63 pages/cpu s221184 r8192 d28672 u262144
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963212] pcpu-alloc: s221184 r8192 d28672 u262144 alloc=1*2097152
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963219] pcpu-alloc: [0] 000 001 002 003 004 005 006 007 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963230] pcpu-alloc: [0] 008 009 010 011 012 013 014 015 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963240] pcpu-alloc: [0] 016 017 018 019 020 021 022 023 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963250] pcpu-alloc: [0] 024 025 026 027 028 029 030 031 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963260] pcpu-alloc: [0] 032 033 034 035 036 037 038 039 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963269] pcpu-alloc: [0] 040 041 042 043 044 045 046 047 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963278] pcpu-alloc: [0] 048 049 050 051 052 053 054 055 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963288] pcpu-alloc: [0] 056 057 058 059 060 061 062 063 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963297] pcpu-alloc: [0] 064 065 066 067 068 069 070 071 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963307] pcpu-alloc: [0] 072 073 074 075 076 077 078 079 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963316] pcpu-alloc: [0] 080 081 082 083 084 085 086 087 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963326] pcpu-alloc: [0] 088 089 090 091 092 093 094 095 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963335] pcpu-alloc: [0] 096 097 098 099 100 101 102 103 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963345] pcpu-alloc: [0] 104 105 106 107 108 109 110 111 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963354] pcpu-alloc: [0] 112 113 114 115 116 117 118 119 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963364] pcpu-alloc: [0] 120 121 122 123 124 125 126 127 
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963489] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic root=UUID=4a64a517-67dd-4c66-898a-7aec80564857 ro find_preseed=/preseed.cfg auto noprompt priority=critical locale=en_US quiet splash
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963711] Unknown kernel command line parameters "auto noprompt splash BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic find_preseed=/preseed.cfg priority=critical locale=en_US", will be passed to user space.
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963754] random: crng init done
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963756] printk: log_buf_len individual max cpu contribution: 4096 bytes
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963759] printk: log_buf_len total cpu_extra contributions: 520192 bytes
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.963761] printk: log_buf_len min size: 262144 bytes
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.010000] printk: log_buf_len: 1048576 bytes
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.010007] printk: early log buf free: 237936(90%)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.048998] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.067812] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.075818] Fallback order for Node 0: 0 
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.075837] Built 1 zonelists, mobility grouping on.  Total pages: 1031888
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.075840] Policy zone: Normal
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.075850] mem auto-init: stack:all(zero), heap alloc:on, heap free:off
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.075857] software IO TLB: area num 128.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.389641] Memory: 3886688K/4193716K available (20480K kernel code, 4264K rwdata, 13180K rodata, 4792K init, 17396K bss, 306768K reserved, 0K cma-reserved)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.391698] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=128, Nodes=1
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.392526] ftrace: allocating 55206 entries in 216 pages
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.410696] ftrace: allocated 216 pages with 4 groups
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.414802] Dynamic Preempt: voluntary
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.415748] rcu: Preemptible hierarchical RCU implementation.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.415752] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=128.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.415756] 	Trampoline variant of Tasks RCU enabled.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.415757] 	Rude variant of Tasks RCU enabled.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.415757] 	Tracing variant of Tasks RCU enabled.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.415758] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.415760] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=128
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.428162] NR_IRQS: 524544, nr_irqs: 1448, preallocated irqs: 16
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.429019] rcu: srcu_init: Setting srcu_struct sizes to big.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.434674] Console: colour VGA+ 80x25
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.434682] printk: console [tty0] enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.435050] ACPI: Core revision 20230331
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.436747] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.436959] APIC: Switch to symmetric I/O mode setup
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.438799] x2apic enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.439502] Switched APIC routing to physical x2apic.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.443489] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.443805] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x22df12c5959, max_idle_ns: 440795242016 ns
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.443828] Calibrating delay loop (skipped) preset value.. 4838.40 BogoMIPS (lpj=9676808)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.444121] x86/cpu: User Mode Instruction Prevention (UMIP) activated
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.444545] Last level iTLB entries: 4KB 0, 2MB 0, 4MB 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.444551] Last level dTLB entries: 4KB 0, 2MB 0, 4MB 0, 1GB 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.444563] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447835] Spectre V2 : Mitigation: Enhanced / Automatic IBRS
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447841] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447844] Spectre V2 : Spectre v2 / PBRSB-eIBRS: Retire a single CALL on VMEXIT
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447853] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447858] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447862] MMIO Stale Data: Unknown: No mitigations
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447887] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447889] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447890] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447891] x86/fpu: Supporting XSAVE feature 0x200: 'Protection Keys User registers'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447892] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447894] x86/fpu: xstate_offset[9]:  832, xstate_sizes[9]:    8
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.447895] x86/fpu: Enabled xstate features 0x207, context size is 840 bytes, using 'compacted' format.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.486650] Freeing SMP alternatives memory: 44K
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.486659] pid_max: default: 131072 minimum: 1024
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.486885] LSM: initializing lsm=lockdown,capability,landlock,yama,apparmor,integrity
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.486982] landlock: Up and running.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.486984] Yama: becoming mindful.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.487388] AppArmor: AppArmor initialized
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.488479] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.488950] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.497610] smpboot: CPU0: Intel(R) Core(TM) i7-14650HX (family: 0x6, model: 0xb7, stepping: 0x1)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] RCU Tasks: Setting shift to 7 and lim to 1 rcu_task_cb_adjust=1.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] RCU Tasks Rude: Setting shift to 7 and lim to 1 rcu_task_cb_adjust=1.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] RCU Tasks Trace: Setting shift to 7 and lim to 1 rcu_task_cb_adjust=1.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] Performance Events: Alderlake Hybrid events, core PMU driver.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: CPUID marked event: 'cpu cycles' unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: CPUID marked event: 'instructions' unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: CPUID marked event: 'bus cycles' unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: CPUID marked event: 'cache references' unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: CPUID marked event: 'cache misses' unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: CPUID marked event: 'branch instructions' unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: CPUID marked event: 'branch misses' unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] core: cpu_core PMU driver: 
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] ... version:                1
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] ... bit width:              48
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] ... generic registers:      6
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] ... value mask:             0000ffffffffffff
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] ... max period:             000000007fffffff
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] ... fixed-purpose events:   0
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] ... event mask:             0001000f0000003f
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499820] signal: max sigframe size: 3632
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499970] rcu: Hierarchical SRCU implementation.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.499973] rcu: 	Max phase no-delay instances is 1000.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.502471] NMI watchdog: Perf NMI watchdog permanently disabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.534552] smp: Bringing up secondary CPUs ...
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.536818] smpboot: x86: Booting SMP configuration:
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.536822] .... node  #0, CPUs:          #1   #2   #3
Jun 30 05:38:40 ty-virtual-machine kernel: [    0.018440] smpboot: CPU 2 Converting physical 0 to logical die 1
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.544419] smp: Brought up 1 node, 4 CPUs
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.544424] smpboot: Max logical packages: 64
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.544425] smpboot: Total of 4 processors activated (19353.61 BogoMIPS)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.548152] devtmpfs: initialized
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.548152] x86/mm: Memory block size: 128MB
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.552339] ACPI: PM: Registering ACPI NVS region [mem 0xbfeff000-0xbfefffff] (4096 bytes)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.552453] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.568147] futex hash table entries: 32768 (order: 9, 2097152 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.568810] pinctrl core: initialized pinctrl subsystem
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.569337] PM: RTC time: 09:38:28, date: 2026-06-30
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.588365] NET: Registered PF_NETLINK/PF_ROUTE protocol family
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593204] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593677] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593785] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593852] audit: initializing netlink subsys (disabled)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] audit: type=2000 audit(1782812308.148:1): state=initialized audit_enabled=0 res=1
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] thermal_sys: Registered thermal governor 'fair_share'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] thermal_sys: Registered thermal governor 'bang_bang'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] thermal_sys: Registered thermal governor 'step_wise'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] thermal_sys: Registered thermal governor 'user_space'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] thermal_sys: Registered thermal governor 'power_allocator'
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] EISA bus registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.593898] cpuidle: using governor ladder
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.595984] cpuidle: using governor menu
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.595990] Simple Boot Flag at 0x36 set to 0x80
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.596054] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.596835] PCI: MMCONFIG for domain 0000 [bus 00-7f] at [mem 0xf0000000-0xf7ffffff] (base 0xf0000000)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.596841] PCI: MMCONFIG at [mem 0xf0000000-0xf7ffffff] reserved as E820 entry
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.596850] PCI: Using configuration type 1 for base access
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.597817] kprobes: kprobe jump-optimization is enabled. All kprobes are optimized if possible.
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.601478] HugeTLB: registered 1.00 GiB page size, pre-allocated 0 pages
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.601478] HugeTLB: 16380 KiB vmemmap can be freed for a 1.00 GiB page
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.601478] HugeTLB: registered 2.00 MiB page size, pre-allocated 0 pages
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.601478] HugeTLB: 28 KiB vmemmap can be freed for a 2.00 MiB page
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.607847] ACPI: Added _OSI(Module Device)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.607852] ACPI: Added _OSI(Processor Device)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.607854] ACPI: Added _OSI(3.0 _SCP Extensions)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.607856] ACPI: Added _OSI(Processor Aggregator Device)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.629338] ACPI: 1 ACPI AML tables successfully acquired and loaded
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.630790] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.662948] ACPI: Interpreter enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.662962] ACPI: PM: (supports S0 S1 S4 S5)
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.662963] ACPI: Using IOAPIC for interrupt routing
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.663820] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.663820] PCI: Using E820 reservations for host bridge windows
Jun 30 05:38:40 ty-virtual-machine kernel: [    1.663820] ACPI: Enabled 4 GPEs in block 00 to 0F
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.076377] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-7f])
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.076394] acpi PNP0A03:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI EDR HPX-Type3]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.076558] acpi PNP0A03:00: _OSC: platform does not support [AER LTR DPC]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.076880] acpi PNP0A03:00: _OSC: OS now controls [PCIeHotplug SHPCHotplug PME PCIeCapability]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.080941] PCI host bridge to bus 0000:00
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.080945] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.080949] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000dbfff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.080951] pci_bus 0000:00: root bus resource [mem 0xc0000000-0xfebfffff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.080953] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.080955] pci_bus 0000:00: root bus resource [io  0x0d00-0xfeff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.080957] pci_bus 0000:00: root bus resource [bus 00-7f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.081139] pci 0000:00:00.0: [8086:7190] type 00 class 0x060000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.082514] pci 0000:00:01.0: [8086:7191] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.086127] pci 0000:00:07.0: [8086:7110] type 00 class 0x060100
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.088289] pci 0000:00:07.1: [8086:7111] type 00 class 0x01018a
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.091375] pci 0000:00:07.1: reg 0x20: [io  0x1060-0x106f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.092646] pci 0000:00:07.1: legacy IDE quirk: reg 0x10: [io  0x01f0-0x01f7]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.092655] pci 0000:00:07.1: legacy IDE quirk: reg 0x14: [io  0x03f6]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.092658] pci 0000:00:07.1: legacy IDE quirk: reg 0x18: [io  0x0170-0x0177]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.092661] pci 0000:00:07.1: legacy IDE quirk: reg 0x1c: [io  0x0376]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.093300] pci 0000:00:07.3: [8086:7113] type 00 class 0x068000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.096134] pci 0000:00:07.3: quirk: [io  0x1000-0x103f] claimed by PIIX4 ACPI
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.096147] pci 0000:00:07.3: quirk: [io  0x1040-0x104f] claimed by PIIX4 SMB
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.096711] pci 0000:00:07.7: [15ad:0740] type 00 class 0x088000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.097899] pci 0000:00:07.7: reg 0x10: [io  0x1080-0x10bf]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.098433] pci 0000:00:07.7: reg 0x14: [mem 0xfebc0000-0xfebfffff 64bit]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.101484] pci 0000:00:0f.0: [15ad:0405] type 00 class 0x030000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.102160] pci 0000:00:0f.0: reg 0x10: [io  0x1070-0x107f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.102763] pci 0000:00:0f.0: reg 0x14: [mem 0xe8000000-0xefffffff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.103315] pci 0000:00:0f.0: reg 0x18: [mem 0xfe000000-0xfe7fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.105570] pci 0000:00:0f.0: reg 0x30: [mem 0x00000000-0x00007fff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.105621] pci 0000:00:0f.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.105979] pci 0000:00:10.0: [1000:0030] type 00 class 0x010000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.106476] pci 0000:00:10.0: reg 0x10: [io  0x1400-0x14ff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.106812] pci 0000:00:10.0: reg 0x14: [mem 0xfeb80000-0xfeb9ffff 64bit]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.107259] pci 0000:00:10.0: reg 0x1c: [mem 0xfeba0000-0xfebbffff 64bit]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.107822] pci 0000:00:10.0: reg 0x30: [mem 0x00000000-0x00003fff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.108202] pci 0000:00:11.0: [15ad:0790] type 01 class 0x060401
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.109293] pci 0000:00:15.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.110322] pci 0000:00:15.0: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.110991] pci 0000:00:15.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.112243] pci 0000:00:15.1: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.112980] pci 0000:00:15.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.114444] pci 0000:00:15.2: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.115646] pci 0000:00:15.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.115646] pci 0000:00:15.3: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.115646] pci 0000:00:15.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.115820] pci 0000:00:15.4: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.115820] pci 0000:00:15.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.119900] pci 0000:00:15.5: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.121176] pci 0000:00:15.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.123109] pci 0000:00:15.6: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.124593] pci 0000:00:15.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.126760] pci 0000:00:15.7: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.127979] pci 0000:00:16.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.129914] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.131140] pci 0000:00:16.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.133084] pci 0000:00:16.1: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine wpa_supplicant[769]: Successfully initialized wpa_supplicant
Jun 30 05:38:40 ty-virtual-machine udisksd[765]: udisks daemon version 2.9.4 starting
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started WPA supplicant.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Network.
Jun 30 05:38:40 ty-virtual-machine apport[715]:    ...done.
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.134388] pci 0000:00:16.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.136291] pci 0000:00:16.2: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.137525] pci 0000:00:16.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.139623] pci 0000:00:16.3: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.140923] pci 0000:00:16.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.142859] pci 0000:00:16.4: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.144014] pci 0000:00:16.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.145913] pci 0000:00:16.5: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.147125] pci 0000:00:16.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.149027] pci 0000:00:16.6: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.150556] pci 0000:00:16.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.152458] pci 0000:00:16.7: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.153597] pci 0000:00:17.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.155492] pci 0000:00:17.0: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.156940] pci 0000:00:17.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.158889] pci 0000:00:17.1: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.160123] pci 0000:00:17.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.162038] pci 0000:00:17.2: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.163215] pci 0000:00:17.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.163215] pci 0000:00:17.3: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.163215] pci 0000:00:17.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.163820] pci 0000:00:17.4: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.163820] pci 0000:00:17.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.163820] pci 0000:00:17.5: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.168596] pci 0000:00:17.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.170659] pci 0000:00:17.6: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.172334] pci 0000:00:17.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.174520] pci 0000:00:17.7: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.175947] pci 0000:00:18.0: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.177928] pci 0000:00:18.0: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.179315] pci 0000:00:18.1: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.181282] pci 0000:00:18.1: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.183099] pci 0000:00:18.2: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.185485] pci 0000:00:18.2: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.186761] pci 0000:00:18.3: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.188676] pci 0000:00:18.3: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.189837] pci 0000:00:18.4: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.191790] pci 0000:00:18.4: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.193013] pci 0000:00:18.5: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.196684] pci 0000:00:18.5: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.198065] pci 0000:00:18.6: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.200834] pci 0000:00:18.6: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.202077] pci 0000:00:18.7: [15ad:07a0] type 01 class 0x060400
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.204390] pci 0000:00:18.7: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.209224] pci_bus 0000:01: extended config space not accessible
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.224162] pci 0000:00:01.0: PCI bridge to [bus 01]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.224668] pci_bus 0000:02: extended config space not accessible
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225378] acpiphp: Slot [32] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225426] acpiphp: Slot [33] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225468] acpiphp: Slot [34] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225511] acpiphp: Slot [35] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225552] acpiphp: Slot [36] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225594] acpiphp: Slot [37] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225679] acpiphp: Slot [38] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225720] acpiphp: Slot [39] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225761] acpiphp: Slot [40] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225801] acpiphp: Slot [41] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225840] acpiphp: Slot [42] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225880] acpiphp: Slot [43] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225919] acpiphp: Slot [44] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.225959] acpiphp: Slot [45] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226040] acpiphp: Slot [46] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226082] acpiphp: Slot [47] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226123] acpiphp: Slot [48] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226163] acpiphp: Slot [49] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226203] acpiphp: Slot [50] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226242] acpiphp: Slot [51] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226282] acpiphp: Slot [52] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226321] acpiphp: Slot [53] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226478] acpiphp: Slot [54] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226524] acpiphp: Slot [55] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226610] acpiphp: Slot [56] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226651] acpiphp: Slot [57] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226683] acpiphp: Slot [58] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226711] acpiphp: Slot [59] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226742] acpiphp: Slot [60] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226777] acpiphp: Slot [61] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226854] acpiphp: Slot [62] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.226884] acpiphp: Slot [63] registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.227007] pci 0000:02:00.0: [15ad:0774] type 00 class 0x0c0300
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.231733] pci 0000:02:00.0: reg 0x20: [io  0x2080-0x209f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.236042] pci 0000:02:01.0: [8086:100f] type 00 class 0x020000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.238700] pci 0000:02:01.0: reg 0x10: [mem 0xfd5c0000-0xfd5dffff 64bit]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.239440] pci 0000:02:01.0: reg 0x18: [mem 0xfdff0000-0xfdffffff 64bit]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.239818] pci 0000:02:01.0: reg 0x20: [io  0x2000-0x203f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.240567] pci 0000:02:01.0: reg 0x30: [mem 0x00000000-0x0000ffff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.240868] pci 0000:02:01.0: PME# supported from D0 D3hot D3cold
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.241477] pci 0000:02:02.0: [1274:1371] type 00 class 0x040100
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.241784] pci 0000:02:02.0: reg 0x10: [io  0x2040-0x207f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.249205] pci 0000:02:03.0: [15ad:0770] type 00 class 0x0c0320
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.250499] pci 0000:02:03.0: reg 0x10: [mem 0xfd5ef000-0xfd5effff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.255916] pci 0000:02:04.0: [15ad:07e0] type 00 class 0x010601
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.258027] pci 0000:02:04.0: reg 0x24: [mem 0xfd5ee000-0xfd5eefff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.259070] pci 0000:02:04.0: reg 0x30: [mem 0x00000000-0x0000ffff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.259939] pci 0000:02:04.0: PME# supported from D3hot
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.279820] pci 0000:00:11.0: PCI bridge to [bus 02] (subtractive decode)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.279852] pci 0000:00:11.0:   bridge window [io  0x2000-0x3fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.279900] pci 0000:00:11.0:   bridge window [mem 0xfd500000-0xfdffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.279989] pci 0000:00:11.0:   bridge window [mem 0xe7b00000-0xe7ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.279993] pci 0000:00:11.0:   bridge window [mem 0x000a0000-0x000bffff window] (subtractive decode)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.279997] pci 0000:00:11.0:   bridge window [mem 0x000d0000-0x000dbfff window] (subtractive decode)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.279999] pci 0000:00:11.0:   bridge window [mem 0xc0000000-0xfebfffff window] (subtractive decode)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.280002] pci 0000:00:11.0:   bridge window [io  0x0000-0x0cf7 window] (subtractive decode)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.280005] pci 0000:00:11.0:   bridge window [io  0x0d00-0xfeff window] (subtractive decode)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.282013] pci 0000:00:15.0: PCI bridge to [bus 03]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.282067] pci 0000:00:15.0:   bridge window [io  0x4000-0x4fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.282114] pci 0000:00:15.0:   bridge window [mem 0xfd400000-0xfd4fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.282202] pci 0000:00:15.0:   bridge window [mem 0xe7a00000-0xe7afffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.283409] pci 0000:00:15.1: PCI bridge to [bus 04]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.283457] pci 0000:00:15.1:   bridge window [io  0x8000-0x8fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.283503] pci 0000:00:15.1:   bridge window [mem 0xfd000000-0xfd0fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.283590] pci 0000:00:15.1:   bridge window [mem 0xe7600000-0xe76fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.285125] pci 0000:00:15.2: PCI bridge to [bus 05]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.285174] pci 0000:00:15.2:   bridge window [io  0xc000-0xcfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.285220] pci 0000:00:15.2:   bridge window [mem 0xfcc00000-0xfccfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.285307] pci 0000:00:15.2:   bridge window [mem 0xe7200000-0xe72fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.287353] pci 0000:00:15.3: PCI bridge to [bus 06]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.287453] pci 0000:00:15.3:   bridge window [mem 0xfc800000-0xfc8fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.287607] pci 0000:00:15.3:   bridge window [mem 0xe6e00000-0xe6efffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.288672] pci 0000:00:15.4: PCI bridge to [bus 07]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.288778] pci 0000:00:15.4:   bridge window [mem 0xfc400000-0xfc4fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.288872] pci 0000:00:15.4:   bridge window [mem 0xe6a00000-0xe6afffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.290412] pci 0000:00:15.5: PCI bridge to [bus 08]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.290521] pci 0000:00:15.5:   bridge window [mem 0xfc000000-0xfc0fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.290613] pci 0000:00:15.5:   bridge window [mem 0xe6600000-0xe66fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:15.6: PCI bridge to [bus 09]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:15.6:   bridge window [mem 0xfbc00000-0xfbcfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:15.6:   bridge window [mem 0xe6200000-0xe62fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:15.7: PCI bridge to [bus 0a]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:15.7:   bridge window [mem 0xfb800000-0xfb8fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:15.7:   bridge window [mem 0xe5e00000-0xe5efffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.0: PCI bridge to [bus 0b]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.0:   bridge window [io  0x5000-0x5fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.0:   bridge window [mem 0xfd300000-0xfd3fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.0:   bridge window [mem 0xe7900000-0xe79fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.1: PCI bridge to [bus 0c]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.1:   bridge window [io  0x9000-0x9fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.1:   bridge window [mem 0xfcf00000-0xfcffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.1:   bridge window [mem 0xe7500000-0xe75fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.2: PCI bridge to [bus 0d]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.2:   bridge window [io  0xd000-0xdfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.2:   bridge window [mem 0xfcb00000-0xfcbfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.291820] pci 0000:00:16.2:   bridge window [mem 0xe7100000-0xe71fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.296538] pci 0000:00:16.3: PCI bridge to [bus 0e]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.296633] pci 0000:00:16.3:   bridge window [mem 0xfc700000-0xfc7fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.296724] pci 0000:00:16.3:   bridge window [mem 0xe6d00000-0xe6dfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.298352] pci 0000:00:16.4: PCI bridge to [bus 0f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.298450] pci 0000:00:16.4:   bridge window [mem 0xfc300000-0xfc3fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.298539] pci 0000:00:16.4:   bridge window [mem 0xe6900000-0xe69fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.299815] pci 0000:00:16.5: PCI bridge to [bus 10]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.300332] pci 0000:00:16.5:   bridge window [mem 0xfbf00000-0xfbffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.300429] pci 0000:00:16.5:   bridge window [mem 0xe6500000-0xe65fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.301756] pci 0000:00:16.6: PCI bridge to [bus 11]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.301848] pci 0000:00:16.6:   bridge window [mem 0xfbb00000-0xfbbfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.301944] pci 0000:00:16.6:   bridge window [mem 0xe6100000-0xe61fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.303288] pci 0000:00:16.7: PCI bridge to [bus 12]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.303392] pci 0000:00:16.7:   bridge window [mem 0xfb700000-0xfb7fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.303484] pci 0000:00:16.7:   bridge window [mem 0xe5d00000-0xe5dfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.304762] pci 0000:00:17.0: PCI bridge to [bus 13]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.304812] pci 0000:00:17.0:   bridge window [io  0x6000-0x6fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.304859] pci 0000:00:17.0:   bridge window [mem 0xfd200000-0xfd2fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.304947] pci 0000:00:17.0:   bridge window [mem 0xe7800000-0xe78fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.306506] pci 0000:00:17.1: PCI bridge to [bus 14]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.306566] pci 0000:00:17.1:   bridge window [io  0xa000-0xafff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.306617] pci 0000:00:17.1:   bridge window [mem 0xfce00000-0xfcefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.306705] pci 0000:00:17.1:   bridge window [mem 0xe7400000-0xe74fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.307977] pci 0000:00:17.2: PCI bridge to [bus 15]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.308028] pci 0000:00:17.2:   bridge window [io  0xe000-0xefff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.308074] pci 0000:00:17.2:   bridge window [mem 0xfca00000-0xfcafffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.308161] pci 0000:00:17.2:   bridge window [mem 0xe7000000-0xe70fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.309486] pci 0000:00:17.3: PCI bridge to [bus 16]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.309589] pci 0000:00:17.3:   bridge window [mem 0xfc600000-0xfc6fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.309681] pci 0000:00:17.3:   bridge window [mem 0xe6c00000-0xe6cfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.310928] pci 0000:00:17.4: PCI bridge to [bus 17]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.311019] pci 0000:00:17.4:   bridge window [mem 0xfc200000-0xfc2fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.311106] pci 0000:00:17.4:   bridge window [mem 0xe6800000-0xe68fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.312358] pci 0000:00:17.5: PCI bridge to [bus 18]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.312454] pci 0000:00:17.5:   bridge window [mem 0xfbe00000-0xfbefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.312542] pci 0000:00:17.5:   bridge window [mem 0xe6400000-0xe64fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.314312] pci 0000:00:17.6: PCI bridge to [bus 19]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.314418] pci 0000:00:17.6:   bridge window [mem 0xfba00000-0xfbafffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.314510] pci 0000:00:17.6:   bridge window [mem 0xe6000000-0xe60fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.315802] pci 0000:00:17.7: PCI bridge to [bus 1a]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.315894] pci 0000:00:17.7:   bridge window [mem 0xfb600000-0xfb6fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.315981] pci 0000:00:17.7:   bridge window [mem 0xe5c00000-0xe5cfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.317284] pci 0000:00:18.0: PCI bridge to [bus 1b]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.317331] pci 0000:00:18.0:   bridge window [io  0x7000-0x7fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.317377] pci 0000:00:18.0:   bridge window [mem 0xfd100000-0xfd1fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.317464] pci 0000:00:18.0:   bridge window [mem 0xe7700000-0xe77fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.319676] pci 0000:00:18.1: PCI bridge to [bus 1c]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.319727] pci 0000:00:18.1:   bridge window [io  0xb000-0xbfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.319773] pci 0000:00:18.1:   bridge window [mem 0xfcd00000-0xfcdfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.319852] pci 0000:00:18.1:   bridge window [mem 0xe7300000-0xe73fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.321021] pci 0000:00:18.2: PCI bridge to [bus 1d]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.321110] pci 0000:00:18.2:   bridge window [mem 0xfc900000-0xfc9fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.321197] pci 0000:00:18.2:   bridge window [mem 0xe6f00000-0xe6ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.322996] pci 0000:00:18.3: PCI bridge to [bus 1e]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.323087] pci 0000:00:18.3:   bridge window [mem 0xfc500000-0xfc5fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.323175] pci 0000:00:18.3:   bridge window [mem 0xe6b00000-0xe6bfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.324463] pci 0000:00:18.4: PCI bridge to [bus 1f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.324584] pci 0000:00:18.4:   bridge window [mem 0xfc100000-0xfc1fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.324677] pci 0000:00:18.4:   bridge window [mem 0xe6700000-0xe67fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.326008] pci 0000:00:18.5: PCI bridge to [bus 20]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.326101] pci 0000:00:18.5:   bridge window [mem 0xfbd00000-0xfbdfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.326189] pci 0000:00:18.5:   bridge window [mem 0xe6300000-0xe63fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.327868] pci 0000:00:18.6: PCI bridge to [bus 21]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.327942] pci 0000:00:18.6:   bridge window [mem 0xfb900000-0xfb9fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.328005] pci 0000:00:18.6:   bridge window [mem 0xe5f00000-0xe5ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.328919] pci 0000:00:18.7: PCI bridge to [bus 22]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.329014] pci 0000:00:18.7:   bridge window [mem 0xfb500000-0xfb5fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.329102] pci 0000:00:18.7:   bridge window [mem 0xe5b00000-0xe5bfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.339585] ACPI: PCI: Interrupt link LNKA configured for IRQ 9
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.339856] ACPI: PCI: Interrupt link LNKB configured for IRQ 11
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.340048] ACPI: PCI: Interrupt link LNKC configured for IRQ 10
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.340232] ACPI: PCI: Interrupt link LNKD configured for IRQ 7
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.432233] iommu: Default domain type: Translated
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.432233] iommu: DMA domain TLB invalidation policy: lazy mode
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433344] SCSI subsystem initialized
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] libata version 3.00 loaded.
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] ACPI: bus type USB registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] usbcore: registered new interface driver usbfs
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] usbcore: registered new interface driver hub
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] usbcore: registered new device driver usb
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] pps_core: LinuxPPS API ver. 1 registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.433426] PTP clock support registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.436029] EDAC MC: Ver: 3.0.0
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.437336] NetLabel: Initializing
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.437336] NetLabel:  domain hash size = 128
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.437336] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.437336] NetLabel:  unlabeled traffic allowed by default
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.440020] mctp: management component transport protocol core
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.440020] NET: Registered PF_MCTP protocol family
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.440020] PCI: Using ACPI for IRQ routing
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.473992] PCI: pci_cache_line_size set to 64 bytes
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.475486] e820: reserve RAM buffer [mem 0x0009e800-0x0009ffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.475495] e820: reserve RAM buffer [mem 0xbfed0000-0xbfffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.475882] pci 0000:00:0f.0: vgaarb: setting as boot VGA device
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.475887] pci 0000:00:0f.0: vgaarb: bridge control possible
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.475889] pci 0000:00:0f.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.475889] vgaarb: loaded
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.477938] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.477963] hpet0: 16 comparators, 64-bit 14.318180 MHz counter
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.480016] clocksource: Switched to clocksource tsc-early
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.535183] VFS: Disk quotas dquot_6.6.0
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.535281] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.536204] AppArmor: AppArmor Filesystem Enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.536244] pnp: PnP ACPI init
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.536565] system 00:00: [io  0x1000-0x103f] has been reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.536569] system 00:00: [io  0x1040-0x104f] has been reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.536572] system 00:00: [io  0x0cf0-0x0cf1] has been reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.537366] system 00:04: [mem 0xfed00000-0xfed003ff] has been reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.542142] pnp 00:06: [dma 2]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.542956] system 00:07: [io  0xfce0-0xfcff] has been reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.542965] system 00:07: [mem 0xf0000000-0xf7ffffff] has been reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.542970] system 00:07: [mem 0xfe800000-0xfe9fffff] has been reserved
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.609166] pnp: PnP ACPI: found 8 devices
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.638096] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.638718] NET: Registered PF_INET protocol family
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.643391] IP idents hash table entries: 65536 (order: 7, 524288 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.669961] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.672577] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.675086] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.684728] TCP bind hash table entries: 32768 (order: 8, 1048576 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.684863] TCP: Hash tables configured (established 32768 bind 32768)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.690253] MPTCP token hash table entries: 4096 (order: 4, 98304 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.690958] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.691532] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694037] NET: Registered PF_UNIX/PF_LOCAL protocol family
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694052] NET: Registered PF_XDP protocol family
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694078] pci 0000:00:15.3: bridge window [io  0x1000-0x0fff] to [bus 06] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694086] pci 0000:00:15.4: bridge window [io  0x1000-0x0fff] to [bus 07] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694091] pci 0000:00:15.5: bridge window [io  0x1000-0x0fff] to [bus 08] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694097] pci 0000:00:15.6: bridge window [io  0x1000-0x0fff] to [bus 09] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694101] pci 0000:00:15.7: bridge window [io  0x1000-0x0fff] to [bus 0a] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694105] pci 0000:00:16.3: bridge window [io  0x1000-0x0fff] to [bus 0e] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694108] pci 0000:00:16.4: bridge window [io  0x1000-0x0fff] to [bus 0f] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694112] pci 0000:00:16.5: bridge window [io  0x1000-0x0fff] to [bus 10] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694115] pci 0000:00:16.6: bridge window [io  0x1000-0x0fff] to [bus 11] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694118] pci 0000:00:16.7: bridge window [io  0x1000-0x0fff] to [bus 12] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694122] pci 0000:00:17.3: bridge window [io  0x1000-0x0fff] to [bus 16] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694125] pci 0000:00:17.4: bridge window [io  0x1000-0x0fff] to [bus 17] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694128] pci 0000:00:17.5: bridge window [io  0x1000-0x0fff] to [bus 18] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694132] pci 0000:00:17.6: bridge window [io  0x1000-0x0fff] to [bus 19] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694135] pci 0000:00:17.7: bridge window [io  0x1000-0x0fff] to [bus 1a] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694139] pci 0000:00:18.2: bridge window [io  0x1000-0x0fff] to [bus 1d] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694142] pci 0000:00:18.3: bridge window [io  0x1000-0x0fff] to [bus 1e] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694145] pci 0000:00:18.4: bridge window [io  0x1000-0x0fff] to [bus 1f] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694148] pci 0000:00:18.5: bridge window [io  0x1000-0x0fff] to [bus 20] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694151] pci 0000:00:18.6: bridge window [io  0x1000-0x0fff] to [bus 21] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694154] pci 0000:00:18.7: bridge window [io  0x1000-0x0fff] to [bus 22] add_size 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694225] pci 0000:00:10.0: BAR 6: assigned [mem 0xc0000000-0xc0003fff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694234] pci 0000:00:15.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694237] pci 0000:00:15.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694242] pci 0000:00:15.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694244] pci 0000:00:15.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694248] pci 0000:00:15.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694250] pci 0000:00:15.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694253] pci 0000:00:15.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694256] pci 0000:00:15.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694259] pci 0000:00:15.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694261] pci 0000:00:15.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694306] pci 0000:00:16.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694310] pci 0000:00:16.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694313] pci 0000:00:16.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694315] pci 0000:00:16.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694319] pci 0000:00:16.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694321] pci 0000:00:16.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694324] pci 0000:00:16.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694326] pci 0000:00:16.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694330] pci 0000:00:16.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694332] pci 0000:00:16.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694335] pci 0000:00:17.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694338] pci 0000:00:17.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694341] pci 0000:00:17.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694343] pci 0000:00:17.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694347] pci 0000:00:17.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694349] pci 0000:00:17.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694352] pci 0000:00:17.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694354] pci 0000:00:17.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694358] pci 0000:00:17.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694360] pci 0000:00:17.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694363] pci 0000:00:18.2: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694365] pci 0000:00:18.2: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694369] pci 0000:00:18.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694371] pci 0000:00:18.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694374] pci 0000:00:18.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694377] pci 0000:00:18.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694380] pci 0000:00:18.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694382] pci 0000:00:18.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694386] pci 0000:00:18.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694388] pci 0000:00:18.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694391] pci 0000:00:18.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694393] pci 0000:00:18.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694403] pci 0000:00:18.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694405] pci 0000:00:18.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694408] pci 0000:00:18.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694410] pci 0000:00:18.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694414] pci 0000:00:18.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694416] pci 0000:00:18.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694419] pci 0000:00:18.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694422] pci 0000:00:18.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694425] pci 0000:00:18.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694427] pci 0000:00:18.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694431] pci 0000:00:18.2: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694433] pci 0000:00:18.2: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694436] pci 0000:00:17.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694438] pci 0000:00:17.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694442] pci 0000:00:17.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694444] pci 0000:00:17.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694447] pci 0000:00:17.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694450] pci 0000:00:17.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694453] pci 0000:00:17.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694455] pci 0000:00:17.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:17.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:17.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:16.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.7: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.7: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.6: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.6: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.5: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.5: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.4: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.4: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.3: BAR 13: no space for [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:15.3: BAR 13: failed to assign [io  size 0x1000]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694462] pci 0000:00:01.0: PCI bridge to [bus 01]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694839] pci 0000:02:01.0: BAR 6: assigned [mem 0xfd500000-0xfd50ffff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694846] pci 0000:02:04.0: BAR 6: assigned [mem 0xfd510000-0xfd51ffff pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694849] pci 0000:00:11.0: PCI bridge to [bus 02]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694883] pci 0000:00:11.0:   bridge window [io  0x2000-0x3fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.694969] pci 0000:00:11.0:   bridge window [mem 0xfd500000-0xfdffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695016] pci 0000:00:11.0:   bridge window [mem 0xe7b00000-0xe7ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695106] pci 0000:00:15.0: PCI bridge to [bus 03]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695137] pci 0000:00:15.0:   bridge window [io  0x4000-0x4fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695204] pci 0000:00:15.0:   bridge window [mem 0xfd400000-0xfd4fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695250] pci 0000:00:15.0:   bridge window [mem 0xe7a00000-0xe7afffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695441] pci 0000:00:15.1: PCI bridge to [bus 04]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695487] pci 0000:00:15.1:   bridge window [io  0x8000-0x8fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695555] pci 0000:00:15.1:   bridge window [mem 0xfd000000-0xfd0fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695601] pci 0000:00:15.1:   bridge window [mem 0xe7600000-0xe76fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695739] pci 0000:00:15.2: PCI bridge to [bus 05]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695767] pci 0000:00:15.2:   bridge window [io  0xc000-0xcfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695834] pci 0000:00:15.2:   bridge window [mem 0xfcc00000-0xfccfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.695879] pci 0000:00:15.2:   bridge window [mem 0xe7200000-0xe72fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696013] pci 0000:00:15.3: PCI bridge to [bus 06]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696081] pci 0000:00:15.3:   bridge window [mem 0xfc800000-0xfc8fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696127] pci 0000:00:15.3:   bridge window [mem 0xe6e00000-0xe6efffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696261] pci 0000:00:15.4: PCI bridge to [bus 07]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696330] pci 0000:00:15.4:   bridge window [mem 0xfc400000-0xfc4fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696376] pci 0000:00:15.4:   bridge window [mem 0xe6a00000-0xe6afffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696508] pci 0000:00:15.5: PCI bridge to [bus 08]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696576] pci 0000:00:15.5:   bridge window [mem 0xfc000000-0xfc0fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696622] pci 0000:00:15.5:   bridge window [mem 0xe6600000-0xe66fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696755] pci 0000:00:15.6: PCI bridge to [bus 09]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696823] pci 0000:00:15.6:   bridge window [mem 0xfbc00000-0xfbcfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.696869] pci 0000:00:15.6:   bridge window [mem 0xe6200000-0xe62fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697002] pci 0000:00:15.7: PCI bridge to [bus 0a]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697071] pci 0000:00:15.7:   bridge window [mem 0xfb800000-0xfb8fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697117] pci 0000:00:15.7:   bridge window [mem 0xe5e00000-0xe5efffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697247] pci 0000:00:16.0: PCI bridge to [bus 0b]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697274] pci 0000:00:16.0:   bridge window [io  0x5000-0x5fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697341] pci 0000:00:16.0:   bridge window [mem 0xfd300000-0xfd3fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697494] pci 0000:00:16.0:   bridge window [mem 0xe7900000-0xe79fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697694] pci 0000:00:16.1: PCI bridge to [bus 0c]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697713] pci 0000:00:16.1:   bridge window [io  0x9000-0x9fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697764] pci 0000:00:16.1:   bridge window [mem 0xfcf00000-0xfcffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697806] pci 0000:00:16.1:   bridge window [mem 0xe7500000-0xe75fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697943] pci 0000:00:16.2: PCI bridge to [bus 0d]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.697971] pci 0000:00:16.2:   bridge window [io  0xd000-0xdfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698039] pci 0000:00:16.2:   bridge window [mem 0xfcb00000-0xfcbfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698085] pci 0000:00:16.2:   bridge window [mem 0xe7100000-0xe71fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698219] pci 0000:00:16.3: PCI bridge to [bus 0e]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698288] pci 0000:00:16.3:   bridge window [mem 0xfc700000-0xfc7fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698334] pci 0000:00:16.3:   bridge window [mem 0xe6d00000-0xe6dfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698489] pci 0000:00:16.4: PCI bridge to [bus 0f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698559] pci 0000:00:16.4:   bridge window [mem 0xfc300000-0xfc3fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698605] pci 0000:00:16.4:   bridge window [mem 0xe6900000-0xe69fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698733] pci 0000:00:16.5: PCI bridge to [bus 10]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698783] pci 0000:00:16.5:   bridge window [mem 0xfbf00000-0xfbffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698816] pci 0000:00:16.5:   bridge window [mem 0xe6500000-0xe65fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698924] pci 0000:00:16.6: PCI bridge to [bus 11]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.698974] pci 0000:00:16.6:   bridge window [mem 0xfbb00000-0xfbbfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699008] pci 0000:00:16.6:   bridge window [mem 0xe6100000-0xe61fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699106] pci 0000:00:16.7: PCI bridge to [bus 12]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699155] pci 0000:00:16.7:   bridge window [mem 0xfb700000-0xfb7fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699191] pci 0000:00:16.7:   bridge window [mem 0xe5d00000-0xe5dfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699340] pci 0000:00:17.0: PCI bridge to [bus 13]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699368] pci 0000:00:17.0:   bridge window [io  0x6000-0x6fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699435] pci 0000:00:17.0:   bridge window [mem 0xfd200000-0xfd2fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699468] pci 0000:00:17.0:   bridge window [mem 0xe7800000-0xe78fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699564] pci 0000:00:17.1: PCI bridge to [bus 14]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699583] pci 0000:00:17.1:   bridge window [io  0xa000-0xafff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699631] pci 0000:00:17.1:   bridge window [mem 0xfce00000-0xfcefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699664] pci 0000:00:17.1:   bridge window [mem 0xe7400000-0xe74fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699760] pci 0000:00:17.2: PCI bridge to [bus 15]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699779] pci 0000:00:17.2:   bridge window [io  0xe000-0xefff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699826] pci 0000:00:17.2:   bridge window [mem 0xfca00000-0xfcafffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699859] pci 0000:00:17.2:   bridge window [mem 0xe7000000-0xe70fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699951] pci 0000:00:17.3: PCI bridge to [bus 16]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.699981] pci 0000:00:17.3:   bridge window [mem 0xfc600000-0xfc6fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700001] pci 0000:00:17.3:   bridge window [mem 0xe6c00000-0xe6cfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700118] pci 0000:00:17.4: PCI bridge to [bus 17]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700187] pci 0000:00:17.4:   bridge window [mem 0xfc200000-0xfc2fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700233] pci 0000:00:17.4:   bridge window [mem 0xe6800000-0xe68fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700365] pci 0000:00:17.5: PCI bridge to [bus 18]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700434] pci 0000:00:17.5:   bridge window [mem 0xfbe00000-0xfbefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700480] pci 0000:00:17.5:   bridge window [mem 0xe6400000-0xe64fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700612] pci 0000:00:17.6: PCI bridge to [bus 19]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700681] pci 0000:00:17.6:   bridge window [mem 0xfba00000-0xfbafffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700727] pci 0000:00:17.6:   bridge window [mem 0xe6000000-0xe60fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700859] pci 0000:00:17.7: PCI bridge to [bus 1a]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700930] pci 0000:00:17.7:   bridge window [mem 0xfb600000-0xfb6fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.700977] pci 0000:00:17.7:   bridge window [mem 0xe5c00000-0xe5cfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701113] pci 0000:00:18.0: PCI bridge to [bus 1b]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701139] pci 0000:00:18.0:   bridge window [io  0x7000-0x7fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701206] pci 0000:00:18.0:   bridge window [mem 0xfd100000-0xfd1fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701329] pci 0000:00:18.0:   bridge window [mem 0xe7700000-0xe77fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701493] pci 0000:00:18.1: PCI bridge to [bus 1c]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701521] pci 0000:00:18.1:   bridge window [io  0xb000-0xbfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701588] pci 0000:00:18.1:   bridge window [mem 0xfcd00000-0xfcdfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701634] pci 0000:00:18.1:   bridge window [mem 0xe7300000-0xe73fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701771] pci 0000:00:18.2: PCI bridge to [bus 1d]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701840] pci 0000:00:18.2:   bridge window [mem 0xfc900000-0xfc9fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.701886] pci 0000:00:18.2:   bridge window [mem 0xe6f00000-0xe6ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702023] pci 0000:00:18.3: PCI bridge to [bus 1e]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702092] pci 0000:00:18.3:   bridge window [mem 0xfc500000-0xfc5fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702139] pci 0000:00:18.3:   bridge window [mem 0xe6b00000-0xe6bfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702273] pci 0000:00:18.4: PCI bridge to [bus 1f]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702342] pci 0000:00:18.4:   bridge window [mem 0xfc100000-0xfc1fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702388] pci 0000:00:18.4:   bridge window [mem 0xe6700000-0xe67fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702546] pci 0000:00:18.5: PCI bridge to [bus 20]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702616] pci 0000:00:18.5:   bridge window [mem 0xfbd00000-0xfbdfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702663] pci 0000:00:18.5:   bridge window [mem 0xe6300000-0xe63fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702821] pci 0000:00:18.6: PCI bridge to [bus 21]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.702975] pci 0000:00:18.6:   bridge window [mem 0xfb900000-0xfb9fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703014] pci 0000:00:18.6:   bridge window [mem 0xe5f00000-0xe5ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703147] pci 0000:00:18.7: PCI bridge to [bus 22]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703215] pci 0000:00:18.7:   bridge window [mem 0xfb500000-0xfb5fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703255] pci 0000:00:18.7:   bridge window [mem 0xe5b00000-0xe5bfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703382] pci_bus 0000:00: resource 4 [mem 0x000a0000-0x000bffff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703389] pci_bus 0000:00: resource 5 [mem 0x000d0000-0x000dbfff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703391] pci_bus 0000:00: resource 6 [mem 0xc0000000-0xfebfffff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703393] pci_bus 0000:00: resource 7 [io  0x0000-0x0cf7 window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703395] pci_bus 0000:00: resource 8 [io  0x0d00-0xfeff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703399] pci_bus 0000:02: resource 0 [io  0x2000-0x3fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703401] pci_bus 0000:02: resource 1 [mem 0xfd500000-0xfdffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703403] pci_bus 0000:02: resource 2 [mem 0xe7b00000-0xe7ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703405] pci_bus 0000:02: resource 4 [mem 0x000a0000-0x000bffff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703406] pci_bus 0000:02: resource 5 [mem 0x000d0000-0x000dbfff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703408] pci_bus 0000:02: resource 6 [mem 0xc0000000-0xfebfffff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703410] pci_bus 0000:02: resource 7 [io  0x0000-0x0cf7 window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703412] pci_bus 0000:02: resource 8 [io  0x0d00-0xfeff window]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703414] pci_bus 0000:03: resource 0 [io  0x4000-0x4fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703416] pci_bus 0000:03: resource 1 [mem 0xfd400000-0xfd4fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703418] pci_bus 0000:03: resource 2 [mem 0xe7a00000-0xe7afffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703420] pci_bus 0000:04: resource 0 [io  0x8000-0x8fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703422] pci_bus 0000:04: resource 1 [mem 0xfd000000-0xfd0fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703423] pci_bus 0000:04: resource 2 [mem 0xe7600000-0xe76fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703425] pci_bus 0000:05: resource 0 [io  0xc000-0xcfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703427] pci_bus 0000:05: resource 1 [mem 0xfcc00000-0xfccfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703429] pci_bus 0000:05: resource 2 [mem 0xe7200000-0xe72fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703432] pci_bus 0000:06: resource 1 [mem 0xfc800000-0xfc8fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703435] pci_bus 0000:06: resource 2 [mem 0xe6e00000-0xe6efffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703438] pci_bus 0000:07: resource 1 [mem 0xfc400000-0xfc4fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703440] pci_bus 0000:07: resource 2 [mem 0xe6a00000-0xe6afffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703443] pci_bus 0000:08: resource 1 [mem 0xfc000000-0xfc0fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703445] pci_bus 0000:08: resource 2 [mem 0xe6600000-0xe66fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703448] pci_bus 0000:09: resource 1 [mem 0xfbc00000-0xfbcfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703450] pci_bus 0000:09: resource 2 [mem 0xe6200000-0xe62fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703453] pci_bus 0000:0a: resource 1 [mem 0xfb800000-0xfb8fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703455] pci_bus 0000:0a: resource 2 [mem 0xe5e00000-0xe5efffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703458] pci_bus 0000:0b: resource 0 [io  0x5000-0x5fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703461] pci_bus 0000:0b: resource 1 [mem 0xfd300000-0xfd3fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703463] pci_bus 0000:0b: resource 2 [mem 0xe7900000-0xe79fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703466] pci_bus 0000:0c: resource 0 [io  0x9000-0x9fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703468] pci_bus 0000:0c: resource 1 [mem 0xfcf00000-0xfcffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703470] pci_bus 0000:0c: resource 2 [mem 0xe7500000-0xe75fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703473] pci_bus 0000:0d: resource 0 [io  0xd000-0xdfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703475] pci_bus 0000:0d: resource 1 [mem 0xfcb00000-0xfcbfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703478] pci_bus 0000:0d: resource 2 [mem 0xe7100000-0xe71fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703480] pci_bus 0000:0e: resource 1 [mem 0xfc700000-0xfc7fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703483] pci_bus 0000:0e: resource 2 [mem 0xe6d00000-0xe6dfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703486] pci_bus 0000:0f: resource 1 [mem 0xfc300000-0xfc3fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703488] pci_bus 0000:0f: resource 2 [mem 0xe6900000-0xe69fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703491] pci_bus 0000:10: resource 1 [mem 0xfbf00000-0xfbffffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703493] pci_bus 0000:10: resource 2 [mem 0xe6500000-0xe65fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703496] pci_bus 0000:11: resource 1 [mem 0xfbb00000-0xfbbfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703498] pci_bus 0000:11: resource 2 [mem 0xe6100000-0xe61fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703501] pci_bus 0000:12: resource 1 [mem 0xfb700000-0xfb7fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703503] pci_bus 0000:12: resource 2 [mem 0xe5d00000-0xe5dfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703506] pci_bus 0000:13: resource 0 [io  0x6000-0x6fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703508] pci_bus 0000:13: resource 1 [mem 0xfd200000-0xfd2fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703510] pci_bus 0000:13: resource 2 [mem 0xe7800000-0xe78fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703513] pci_bus 0000:14: resource 0 [io  0xa000-0xafff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703515] pci_bus 0000:14: resource 1 [mem 0xfce00000-0xfcefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703518] pci_bus 0000:14: resource 2 [mem 0xe7400000-0xe74fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703520] pci_bus 0000:15: resource 0 [io  0xe000-0xefff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703522] pci_bus 0000:15: resource 1 [mem 0xfca00000-0xfcafffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703525] pci_bus 0000:15: resource 2 [mem 0xe7000000-0xe70fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703527] pci_bus 0000:16: resource 1 [mem 0xfc600000-0xfc6fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703530] pci_bus 0000:16: resource 2 [mem 0xe6c00000-0xe6cfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703532] pci_bus 0000:17: resource 1 [mem 0xfc200000-0xfc2fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703535] pci_bus 0000:17: resource 2 [mem 0xe6800000-0xe68fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703538] pci_bus 0000:18: resource 1 [mem 0xfbe00000-0xfbefffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703540] pci_bus 0000:18: resource 2 [mem 0xe6400000-0xe64fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703543] pci_bus 0000:19: resource 1 [mem 0xfba00000-0xfbafffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703545] pci_bus 0000:19: resource 2 [mem 0xe6000000-0xe60fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703548] pci_bus 0000:1a: resource 1 [mem 0xfb600000-0xfb6fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703550] pci_bus 0000:1a: resource 2 [mem 0xe5c00000-0xe5cfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703553] pci_bus 0000:1b: resource 0 [io  0x7000-0x7fff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703555] pci_bus 0000:1b: resource 1 [mem 0xfd100000-0xfd1fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703557] pci_bus 0000:1b: resource 2 [mem 0xe7700000-0xe77fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703560] pci_bus 0000:1c: resource 0 [io  0xb000-0xbfff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703562] pci_bus 0000:1c: resource 1 [mem 0xfcd00000-0xfcdfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703565] pci_bus 0000:1c: resource 2 [mem 0xe7300000-0xe73fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703567] pci_bus 0000:1d: resource 1 [mem 0xfc900000-0xfc9fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703570] pci_bus 0000:1d: resource 2 [mem 0xe6f00000-0xe6ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703572] pci_bus 0000:1e: resource 1 [mem 0xfc500000-0xfc5fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703575] pci_bus 0000:1e: resource 2 [mem 0xe6b00000-0xe6bfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703577] pci_bus 0000:1f: resource 1 [mem 0xfc100000-0xfc1fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703580] pci_bus 0000:1f: resource 2 [mem 0xe6700000-0xe67fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703582] pci_bus 0000:20: resource 1 [mem 0xfbd00000-0xfbdfffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703585] pci_bus 0000:20: resource 2 [mem 0xe6300000-0xe63fffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703587] pci_bus 0000:21: resource 1 [mem 0xfb900000-0xfb9fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703590] pci_bus 0000:21: resource 2 [mem 0xe5f00000-0xe5ffffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703592] pci_bus 0000:22: resource 1 [mem 0xfb500000-0xfb5fffff]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.703595] pci_bus 0000:22: resource 2 [mem 0xe5b00000-0xe5bfffff 64bit pref]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.704106] pci 0000:00:00.0: Limiting direct PCI/PCI transfers
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.707055] pci 0000:02:01.0: CLS mismatch (32 != 64), using 64 bytes
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.709053] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.709058] software IO TLB: mapped [mem 0x00000000bbed0000-0x00000000bfed0000] (64MB)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.709182] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x22df12c5959, max_idle_ns: 440795242016 ns
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.709505] clocksource: Switched to clocksource tsc
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.710742] Trying to unpack rootfs image as initramfs...
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.719188] Initialise system trusted keyrings
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.719206] Key type blacklist registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.720054] workingset: timestamp_bits=36 max_order=20 bucket_order=0
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.720082] zbud: loaded
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.722101] squashfs: version 4.0 (2009/01/31) Phillip Lougher
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.723251] fuse: init (API version 7.38)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.725200] integrity: Platform Keyring initialized
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.725208] integrity: Machine keyring initialized
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.741509] Key type asymmetric registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.741518] Asymmetric key parser 'x509' registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.742185] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 243)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.743334] io scheduler mq-deadline registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.746609] pcieport 0000:00:15.0: PME: Signaling with IRQ 24
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.746754] pcieport 0000:00:15.0: pciehp: Slot #160 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.748722] pcieport 0000:00:15.1: PME: Signaling with IRQ 25
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.748775] pcieport 0000:00:15.1: pciehp: Slot #161 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.750842] pcieport 0000:00:15.2: PME: Signaling with IRQ 26
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.750896] pcieport 0000:00:15.2: pciehp: Slot #162 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.754343] pcieport 0000:00:15.3: PME: Signaling with IRQ 27
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.754687] pcieport 0000:00:15.3: pciehp: Slot #163 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.757626] pcieport 0000:00:15.4: PME: Signaling with IRQ 28
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.757797] pcieport 0000:00:15.4: pciehp: Slot #164 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.760813] pcieport 0000:00:15.5: PME: Signaling with IRQ 29
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.761266] pcieport 0000:00:15.5: pciehp: Slot #165 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.764222] pcieport 0000:00:15.6: PME: Signaling with IRQ 30
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.764845] pcieport 0000:00:15.6: pciehp: Slot #166 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.767433] pcieport 0000:00:15.7: PME: Signaling with IRQ 31
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.767709] pcieport 0000:00:15.7: pciehp: Slot #167 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.771593] pcieport 0000:00:16.0: PME: Signaling with IRQ 32
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.771823] pcieport 0000:00:16.0: pciehp: Slot #192 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.775579] pcieport 0000:00:16.1: PME: Signaling with IRQ 33
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.775750] pcieport 0000:00:16.1: pciehp: Slot #193 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.778892] pcieport 0000:00:16.2: PME: Signaling with IRQ 34
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.779269] pcieport 0000:00:16.2: pciehp: Slot #194 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.780766] pcieport 0000:00:16.3: PME: Signaling with IRQ 35
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.780820] pcieport 0000:00:16.3: pciehp: Slot #195 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.784384] pcieport 0000:00:16.4: PME: Signaling with IRQ 36
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.784565] pcieport 0000:00:16.4: pciehp: Slot #196 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.787688] pcieport 0000:00:16.5: PME: Signaling with IRQ 37
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.788088] pcieport 0000:00:16.5: pciehp: Slot #197 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.791498] pcieport 0000:00:16.6: PME: Signaling with IRQ 38
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.791674] pcieport 0000:00:16.6: pciehp: Slot #198 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.795525] pcieport 0000:00:16.7: PME: Signaling with IRQ 39
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.795981] pcieport 0000:00:16.7: pciehp: Slot #199 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.800112] pcieport 0000:00:17.0: PME: Signaling with IRQ 40
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.800293] pcieport 0000:00:17.0: pciehp: Slot #224 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.803975] pcieport 0000:00:17.1: PME: Signaling with IRQ 41
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.804199] pcieport 0000:00:17.1: pciehp: Slot #225 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.807546] pcieport 0000:00:17.2: PME: Signaling with IRQ 42
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.807746] pcieport 0000:00:17.2: pciehp: Slot #226 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.811226] pcieport 0000:00:17.3: PME: Signaling with IRQ 43
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.811458] pcieport 0000:00:17.3: pciehp: Slot #227 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.814219] pcieport 0000:00:17.4: PME: Signaling with IRQ 44
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.814443] pcieport 0000:00:17.4: pciehp: Slot #228 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.817967] pcieport 0000:00:17.5: PME: Signaling with IRQ 45
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.818667] pcieport 0000:00:17.5: pciehp: Slot #229 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.822091] pcieport 0000:00:17.6: PME: Signaling with IRQ 46
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.822328] pcieport 0000:00:17.6: pciehp: Slot #230 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.825301] pcieport 0000:00:17.7: PME: Signaling with IRQ 47
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.825505] pcieport 0000:00:17.7: pciehp: Slot #231 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.827360] pcieport 0000:00:18.0: PME: Signaling with IRQ 48
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.827418] pcieport 0000:00:18.0: pciehp: Slot #256 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.829955] pcieport 0000:00:18.1: PME: Signaling with IRQ 49
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.830130] pcieport 0000:00:18.1: pciehp: Slot #257 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.833254] pcieport 0000:00:18.2: PME: Signaling with IRQ 50
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.833432] pcieport 0000:00:18.2: pciehp: Slot #258 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.836256] pcieport 0000:00:18.3: PME: Signaling with IRQ 51
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.836431] pcieport 0000:00:18.3: pciehp: Slot #259 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.839540] pcieport 0000:00:18.4: PME: Signaling with IRQ 52
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.839718] pcieport 0000:00:18.4: pciehp: Slot #260 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.842963] pcieport 0000:00:18.5: PME: Signaling with IRQ 53
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.843138] pcieport 0000:00:18.5: pciehp: Slot #261 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.846254] pcieport 0000:00:18.6: PME: Signaling with IRQ 54
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.846438] pcieport 0000:00:18.6: pciehp: Slot #262 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.849470] pcieport 0000:00:18.7: PME: Signaling with IRQ 55
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.849736] pcieport 0000:00:18.7: pciehp: Slot #263 AttnBtn+ PwrCtrl+ MRL- AttnInd- PwrInd- HotPlug+ Surprise- Interlock- NoCompl+ IbPresDis- LLActRep+
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.852929] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.854203] ACPI: AC: AC Adapter [ACAD] (on-line)
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.854569] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.854794] ACPI: button: Power Button [PWRF]
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.859105] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.887993] 00:05: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.990485] Linux agpgart interface v0.103
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.990761] agpgart-intel 0000:00:00.0: Intel 440BX Chipset
Jun 30 05:38:40 ty-virtual-machine kernel: [    2.996611] agpgart-intel 0000:00:00.0: AGP aperture is 256M @ 0x0
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.088879] loop: module loaded
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.090273] ata_piix 0000:00:07.1: version 2.13
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.094696] scsi host0: ata_piix
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.096031] scsi host1: ata_piix
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.096322] ata1: PATA max UDMA/33 cmd 0x1f0 ctl 0x3f6 bmdma 0x1060 irq 14
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.096325] ata2: PATA max UDMA/33 cmd 0x170 ctl 0x376 bmdma 0x1068 irq 15
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.096856] tun: Universal TUN/TAP device driver, 1.6
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.097005] PPP generic driver version 2.4.2
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098142] uhci_hcd 0000:02:00.0: UHCI Host Controller
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Modem Manager...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Network Manager Wait Online...
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098149] uhci_hcd 0000:02:00.0: new USB bus registered, assigned bus number 1
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098197] uhci_hcd 0000:02:00.0: detected 2 ports
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098499] uhci_hcd 0000:02:00.0: irq 18, io port 0x00002080
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098864] usb usb1: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 6.05
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098871] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098874] usb usb1: Product: UHCI Host Controller
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098877] usb usb1: Manufacturer: Linux 6.5.0-18-generic uhci_hcd
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.098879] usb usb1: SerialNumber: 0000:02:00.0
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.099378] hub 1-0:1.0: USB hub found
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.099393] hub 1-0:1.0: 2 ports detected
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.100452] ehci-pci 0000:02:03.0: EHCI Host Controller
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.100474] ehci-pci 0000:02:03.0: new USB bus registered, assigned bus number 2
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.100607] i8042: PNP: PS/2 Controller [PNP0303:KBC,PNP0f13:MOUS] at 0x60,0x64 irq 1,12
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.101028] ehci-pci 0000:02:03.0: irq 17, io mem 0xfd5ef000
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.102228] serio: i8042 KBD port at 0x60,0x64 irq 1
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.102243] serio: i8042 AUX port at 0x60,0x64 irq 12
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.103001] mousedev: PS/2 mouse device common for all mice
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.105708] rtc_cmos 00:01: registered as rtc0
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106086] rtc_cmos 00:01: setting system clock to 2026-06-30T09:38:30 UTC (1782812310)
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106347] rtc_cmos 00:01: alarms up to one month, y3k, 114 bytes nvram
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106372] i2c_dev: i2c /dev entries driver
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106409] device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106443] device-mapper: uevent: version 1.0.3
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106675] device-mapper: ioctl: 4.48.0-ioctl (2023-03-01) initialised: dm-devel@redhat.com
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106713] platform eisa.0: Probing EISA bus 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106717] platform eisa.0: EISA: Cannot allocate resource for mainboard
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106721] platform eisa.0: Cannot allocate resource for EISA slot 1
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106723] platform eisa.0: Cannot allocate resource for EISA slot 2
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106726] platform eisa.0: Cannot allocate resource for EISA slot 3
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106728] platform eisa.0: Cannot allocate resource for EISA slot 4
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106730] platform eisa.0: Cannot allocate resource for EISA slot 5
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106732] platform eisa.0: Cannot allocate resource for EISA slot 6
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106734] platform eisa.0: Cannot allocate resource for EISA slot 7
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106736] platform eisa.0: Cannot allocate resource for EISA slot 8
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106738] platform eisa.0: EISA: Detected 0 cards
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.106742] intel_pstate: CPU model not supported
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.107243] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input1
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.107407] ledtrig-cpu: registered to indicate activity on CPUs
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.108145] drop_monitor: Initializing network drop monitor service
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.119459] ehci-pci 0000:02:03.0: USB 2.0 started, EHCI 1.00
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.120277] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.05
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.120286] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.120290] usb usb2: Product: EHCI Host Controller
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.120293] usb usb2: Manufacturer: Linux 6.5.0-18-generic ehci_hcd
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.120296] usb usb2: SerialNumber: 0000:02:03.0
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.121311] hub 2-0:1.0: USB hub found
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.121400] hub 2-0:1.0: 6 ports detected
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.193378] NET: Registered PF_INET6 protocol family
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.338557] usb 1-1: new full-speed USB device number 2 using uhci_hcd
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.498555] usb 1-1: New USB device found, idVendor=0e0f, idProduct=0003, bcdDevice= 1.03
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.498568] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.498572] usb 1-1: Product: VMware Virtual USB Mouse
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.498575] usb 1-1: Manufacturer: VMware
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.631003] usb 1-2: new full-speed USB device number 3 using uhci_hcd
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.791713] usb 1-2: New USB device found, idVendor=0e0f, idProduct=0002, bcdDevice= 1.00
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.791725] usb 1-2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.791729] usb 1-2: Product: VMware Virtual USB Hub
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.791732] usb 1-2: Manufacturer: VMware, Inc.
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.799127] hub 1-2:1.0: USB hub found
Jun 30 05:38:40 ty-virtual-machine kernel: [    3.802385] hub 1-2:1.0: 7 ports detected
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.790715] Freeing initrd memory: 68556K
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.827720] Segment Routing with IPv6
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.827976] In-situ OAM (IOAM) with IPv6
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.828070] NET: Registered PF_PACKET protocol family
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.828895] Key type dns_resolver registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.831839] IPI shorthand broadcast: enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.838157] sched_clock: Marking stable (5820032697, 14440778)->(5934319471, -99845996)
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.839657] registered taskstats version 1
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.862673] Loading compiled-in X.509 certificates
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.864880] Loaded X.509 cert 'Build time autogenerated kernel key: a7207d837189cdb9d766e4ced6907e48f3822488'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.865975] Loaded X.509 cert 'Canonical Ltd. Live Patch Signing: 14df34d1a87cf37625abec039ef2bf521249b969'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867247] Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing: 88f752e560a1e0737e31163a466ad7b70a850c19'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867254] blacklist: Loading compiled-in revocation X.509 certificates
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867293] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing: 61482aa2830d0ab2ad5af10b7250da9033ddcef0'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867322] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2017): 242ade75ac4a15e50d50c84b0d45ff3eae707a03'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867488] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (ESM 2018): 365188c1d374d6b07c3c8f240f8ef722433d6a8b'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867618] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2019): c0746fd6c5da3ae827864651ad66ae47fe24b3e8'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867646] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v1): a8d54bbb3825cfb94fa13c9f8a594a195c107b8d'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.867717] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v2): 4cf046892d6fd3c9a5b03f98d845f90851dc6a8c'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.868026] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.868056] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (Ubuntu Core 2019): c1d57b8f6b743f23ee41f4f7ee292f06eecadfb9'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.880438] Key type .fscrypt registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.880444] Key type fscrypt-provisioning registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.900728] Key type encrypted registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.900742] AppArmor: AppArmor sha1 policy hashing enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.900761] ima: No TPM chip found, activating TPM-bypass!
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.900770] Loading compiled-in module X.509 certificates
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901826] Loaded X.509 cert 'Build time autogenerated kernel key: a7207d837189cdb9d766e4ced6907e48f3822488'
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901830] ima: Allocated hash algorithm: sha1
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901842] ima: No architecture policies found
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901858] evm: Initialising EVM extended attributes:
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901859] evm: security.selinux
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901861] evm: security.SMACK64
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901863] evm: security.SMACK64EXEC
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901864] evm: security.SMACK64TRANSMUTE
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901865] evm: security.SMACK64MMAP
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901866] evm: security.apparmor
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901868] evm: security.ima
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901869] evm: security.capability
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.901870] evm: HMAC attrs: 0x1
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.903896] PM:   Magic number: 14:788:627
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.918861] RAS: Correctable Errors collector initialized.
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.918958] clk: Disabling unused clocks
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.923307] Freeing unused decrypted memory: 2036K
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.924870] Freeing unused kernel image (initmem) memory: 4792K
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.938917] Write protecting the kernel read-only data: 34816k
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.941638] Freeing unused kernel image (rodata/data gap) memory: 1156K
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974052] x86/mm: Checked W+X mappings: passed, no W+X pages found.
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974070] Run /init as init process
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974073]   with arguments:
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974075]     /init
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974077]     auto
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974079]     noprompt
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974080]     splash
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974082]   with environment:
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974083]     HOME=/
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974084]     TERM=linux
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974086]     BOOT_IMAGE=/boot/vmlinuz-6.5.0-18-generic
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974087]     find_preseed=/preseed.cfg
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974089]     priority=critical
Jun 30 05:38:40 ty-virtual-machine kernel: [    5.974090]     locale=en_US
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.566227] Floppy drive(s): fd0 is 1.44M
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.584512] FDC 0 is a post-1991 82077
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.699813] e1000: Intel(R) PRO/1000 Network Driver
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.699873] e1000: Copyright (c) 1999-2006 Intel Corporation.
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.724917] piix4_smbus 0000:00:07.3: SMBus Host Controller not enabled!
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.735048] hid: raw HID events driver (C) Jiri Kosina
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.737527] input: VirtualPS/2 VMware VMMouse as /devices/platform/i8042/serio1/input/input4
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.742754] Fusion MPT base driver 3.04.20
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.742760] Copyright (c) 1999-2008 LSI Corporation
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.746216] ahci 0000:02:04.0: version 3.0
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.757394] input: VirtualPS/2 VMware VMMouse as /devices/platform/i8042/serio1/input/input3
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.764000] ahci 0000:02:04.0: AHCI 0001.0300 32 slots 30 ports 6 Gbps 0x3fffffff impl SATA mode
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.764013] ahci 0000:02:04.0: flags: 64bit ncq clo only 
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.765685] Fusion MPT SPI Host driver 3.04.20
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.767326] mptbase: ioc0: Initiating bringup
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.821032] scsi host2: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.828119] scsi host3: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.838799] scsi host4: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.839774] scsi host5: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.843367] scsi host6: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.844885] scsi host7: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.846874] scsi host8: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.851486] scsi host9: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.857477] scsi host10: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.860829] scsi host11: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.870580] scsi host12: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.871252] scsi host13: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.873463] scsi host14: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.875084] scsi host15: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.877293] scsi host16: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.878837] ioc0: LSI53C1030 B0: Capabilities={Initiator}
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.879199] scsi host17: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.880277] scsi host18: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.881555] scsi host19: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.884383] scsi host20: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.886145] scsi host21: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.887235] scsi host22: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.887965] scsi host23: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.888689] scsi host24: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.890183] scsi host25: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.890782] scsi host26: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.891555] scsi host27: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.893128] scsi host28: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.894318] scsi host29: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.895259] scsi host30: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896072] scsi host31: ahci
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896343] ata3: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee100 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896346] ata4: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee180 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896347] ata5: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee200 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896348] ata6: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee280 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896349] ata7: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee300 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896350] ata8: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee380 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896351] ata9: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee400 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896352] ata10: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee480 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896353] ata11: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee500 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896354] ata12: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee580 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896355] ata13: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee600 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896356] ata14: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee680 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896357] ata15: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee700 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896358] ata16: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee780 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896358] ata17: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee800 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896359] ata18: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee880 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896360] ata19: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee900 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896361] ata20: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5ee980 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896362] ata21: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eea00 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896363] ata22: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eea80 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896364] ata23: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eeb00 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896365] ata24: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eeb80 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896366] ata25: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eec00 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896366] ata26: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eec80 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896367] ata27: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eed00 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896368] ata28: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eed80 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896369] ata29: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eee00 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896370] ata30: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eee80 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896371] ata31: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eef00 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.896372] ata32: SATA max UDMA/133 abar m4096@0xfd5ee000 port 0xfd5eef80 irq 56
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.962596] usbcore: registered new interface driver usbhid
Jun 30 05:38:40 ty-virtual-machine kernel: [    6.962604] usbhid: USB HID core driver
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.133020] scsi host32: ioc0: LSI53C1030 B0, FwRev=01032920h, Ports=1, MaxQ=128, IRQ=17
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.209951] ata5: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.210174] ata3: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.211936] ata4: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.213431] ata4.00: ATAPI: VMware Virtual SATA CDRW Drive, 00000001, max UDMA/33
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.213660] ata10: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.213692] ata4.00: configured for UDMA/33
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.213970] ata3.00: ATAPI: VMware Virtual SATA CDRW Drive, 00000001, max UDMA/33
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.214122] ata7: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.215830] ata6: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.215890] ata11: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.215947] ata8: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216021] ata14: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216045] ata17: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216098] ata20: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216223] ata19: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216250] ata18: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216277] ata9: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216316] ata15: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216372] ata3.00: configured for UDMA/33
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.216451] ata13: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.217799] scsi 2:0:0:0: CD-ROM            NECVMWar VMware SATA CD00 1.00 PQ: 0 ANSI: 5
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.218689] ata24: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.218727] ata21: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.219965] ata16: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.219997] ata25: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.220130] ata12: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.220383] sr 2:0:0:0: [sr0] scsi3-mmc drive: 1x/1x writer dvd-ram cd/rw xa/form2 cdda tray
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.220390] cdrom: Uniform CD-ROM driver Revision: 3.20
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.221452] ata27: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.223513] ata26: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.224887] ata23: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.224947] ata22: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.226554] ata31: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.226618] ata32: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.227520] ata30: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.230422] ata29: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.230797] ata28: SATA link down (SStatus 0 SControl 300)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.233342] e1000 0000:02:01.0 eth0: (PCI:66MHz:32-bit) 00:0c:29:20:05:75
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.233361] e1000 0000:02:01.0 eth0: Intel(R) PRO/1000 Network Connection
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.266468] sr 2:0:0:0: Attached scsi CD-ROM sr0
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.266795] sr 2:0:0:0: Attached scsi generic sg0 type 5
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.267645] scsi 3:0:0:0: CD-ROM            NECVMWar VMware SATA CD01 1.00 PQ: 0 ANSI: 5
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.271106] sr 3:0:0:0: [sr1] scsi3-mmc drive: 1x/1x writer dvd-ram cd/rw xa/form2 cdda tray
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.307562] scsi 32:0:0:0: Direct-Access     VMware,  VMware Virtual S 1.0  PQ: 0 ANSI: 2
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.324681] sr 3:0:0:0: Attached scsi CD-ROM sr1
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.325607] sr 3:0:0:0: Attached scsi generic sg1 type 5
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.326794] scsi target32:0:0: Beginning Domain Validation
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.337103] scsi target32:0:0: Domain Validation skipping write tests
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.337108] scsi target32:0:0: Ending Domain Validation
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.337333] scsi target32:0:0: FAST-40 WIDE SCSI 80.0 MB/s ST (25 ns, offset 127)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.352614] sd 32:0:0:0: Attached scsi generic sg2 type 0
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.353833] sd 32:0:0:0: [sda] 83886080 512-byte logical blocks: (42.9 GB/40.0 GiB)
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.354522] sd 32:0:0:0: [sda] Write Protect is off
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.354531] sd 32:0:0:0: [sda] Mode Sense: 61 00 00 00
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.355079] sd 32:0:0:0: [sda] Cache data unavailable
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.355086] sd 32:0:0:0: [sda] Assuming drive cache: write through
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.372540]  sda: sda1 sda2 sda3
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.373985] sd 32:0:0:0: [sda] Attached SCSI disk
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.410699] e1000 0000:02:01.0 ens33: renamed from eth0
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.410874] input: VMware VMware Virtual USB Mouse as /devices/pci0000:00/0000:00:11.0/0000:02:00.0/usb1/1-1/1-1:1.0/0003:0E0F:0003.0001/input/input5
Jun 30 05:38:40 ty-virtual-machine kernel: [    7.410918] hid-generic 0003:0E0F:0003.0001: input,hidraw0: USB HID v1.10 Mouse [VMware VMware Virtual USB Mouse] on usb-0000:02:00.0-1/input0
Jun 30 05:38:40 ty-virtual-machine kernel: [    8.714023] EXT4-fs (sda3): mounted filesystem 4a64a517-67dd-4c66-898a-7aec80564857 ro with ordered data mode. Quota mode: none.
Jun 30 05:38:40 ty-virtual-machine kernel: [    8.908062] systemd[1]: Inserted module 'autofs4'
Jun 30 05:38:40 ty-virtual-machine kernel: [    8.976366] systemd[1]: systemd 249.11-0ubuntu3.12 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
Jun 30 05:38:40 ty-virtual-machine kernel: [    8.976744] systemd[1]: Detected virtualization vmware.
Jun 30 05:38:40 ty-virtual-machine kernel: [    8.976754] systemd[1]: Detected architecture x86-64.
Jun 30 05:38:40 ty-virtual-machine kernel: [    8.978141] systemd[1]: Hostname set to <ty-virtual-machine>.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.017010] systemd[1]: memfd_create() called without MFD_EXEC or MFD_NOEXEC_SEAL set
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.098567] block sda: the capability attribute has been deprecated.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.337884] systemd[1]: Queued start job for default target Graphical Interface.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.357122] systemd[1]: Created slice Slice /system/modprobe.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.359641] systemd[1]: Created slice Slice /system/systemd-fsck.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360149] systemd[1]: Created slice User and Session Slice.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360301] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360633] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360741] systemd[1]: Reached target User and Group Name Lookups.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360767] systemd[1]: Reached target Remote File Systems.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360786] systemd[1]: Reached target Slice Units.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360809] systemd[1]: Reached target Mounting snaps.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.360852] systemd[1]: Reached target Local Verity Protected Volumes.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.361092] systemd[1]: Listening on Syslog Socket.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.361256] systemd[1]: Listening on fsck to fsckd communication Socket.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.361350] systemd[1]: Listening on initctl Compatibility Named Pipe.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.361649] systemd[1]: Listening on Journal Audit Socket.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.361791] systemd[1]: Listening on Journal Socket (/dev/log).
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.361964] systemd[1]: Listening on Journal Socket.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.362728] systemd[1]: Listening on udev Control Socket.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.362929] systemd[1]: Listening on udev Kernel Socket.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.364786] systemd[1]: Mounting Huge Pages File System...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.366352] systemd[1]: Mounting POSIX Message Queue File System...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.368697] systemd[1]: Mounting Kernel Debug File System...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.372603] systemd[1]: Mounting Kernel Trace File System...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.377728] systemd[1]: Starting Journal Service...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.381064] systemd[1]: Starting Set the console keyboard layout...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.384522] systemd[1]: Starting Create List of Static Device Nodes...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.387739] systemd[1]: Starting Load Kernel Module configfs...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.391195] systemd[1]: Starting Load Kernel Module drm...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.396457] systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.400167] systemd[1]: Starting Load Kernel Module fuse...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.401841] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.408583] systemd[1]: Starting Load Kernel Modules...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.410601] systemd[1]: Starting Remount Root and Kernel File Systems...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.412624] systemd[1]: Starting Coldplug All udev Devices...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.415950] systemd[1]: Mounted Huge Pages File System.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.416158] systemd[1]: Mounted POSIX Message Queue File System.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.416313] systemd[1]: Mounted Kernel Debug File System.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.416459] systemd[1]: Mounted Kernel Trace File System.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.417029] systemd[1]: Finished Create List of Static Device Nodes.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.417610] systemd[1]: modprobe@configfs.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.418015] systemd[1]: Finished Load Kernel Module configfs.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.418469] systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.419192] systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.419657] systemd[1]: modprobe@fuse.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.419878] systemd[1]: Finished Load Kernel Module fuse.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.422860] systemd[1]: Mounting FUSE Control File System...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.429161] systemd[1]: Mounting Kernel Configuration File System...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.441785] systemd[1]: Mounted Kernel Configuration File System.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.442455] systemd[1]: Mounted FUSE Control File System.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.443008] EXT4-fs (sda3): re-mounted 4a64a517-67dd-4c66-898a-7aec80564857 r/w. Quota mode: none.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.445021] systemd[1]: Finished Remount Root and Kernel File Systems.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.447429] systemd[1]: Activating swap /swapfile...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.447640] systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.449564] systemd[1]: Starting Load/Save Random Seed...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.452248] systemd[1]: Starting Create System Users...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.471459] systemd[1]: Finished Load/Save Random Seed.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.471689] systemd[1]: Condition check resulted in First Boot Complete being skipped.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.473585] Adding 3991548k swap on /swapfile.  Priority:-2 extents:9 across:4302844k FS
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.473761] systemd[1]: Activated swap /swapfile.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.473862] systemd[1]: Reached target Swaps.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.474739] lp: driver loaded but no devices found
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.486629] systemd[1]: Finished Create System Users.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.492432] ppdev: user-space parallel port driver
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.527450] systemd[1]: Starting Create Static Device Nodes in /dev...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.528252] ACPI: bus type drm_connector registered
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.528811] systemd[1]: Finished Set the console keyboard layout.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.533205] systemd[1]: modprobe@drm.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.533700] systemd[1]: Finished Load Kernel Module drm.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.540487] systemd[1]: Finished Load Kernel Modules.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.542767] systemd[1]: Starting Apply Kernel Variables...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.552687] systemd[1]: Finished Create Static Device Nodes in /dev.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.552805] systemd[1]: Reached target Preparation for Local File Systems.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.557019] systemd[1]: Mounting Mount unit for bare, revision 5...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.561053] systemd[1]: Mounting Mount unit for core22, revision 1122...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.561075] loop0: detected capacity change from 0 to 8
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.563729] systemd[1]: Mounting Mount unit for firefox, revision 3836...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.566032] systemd[1]: Mounting Mount unit for gnome-42-2204, revision 141...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.568881] systemd[1]: Mounting Mount unit for gtk-common-themes, revision 1535...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.571060] loop1: detected capacity change from 0 to 151992
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.571132] loop2: detected capacity change from 0 to 1017816
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.574141] loop3: detected capacity change from 0 to 546064
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.575982] systemd[1]: Mounting Mount unit for snap-store, revision 959...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.578333] systemd[1]: Mounting Mount unit for snapd, revision 20671...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.580826] systemd[1]: Mounting Mount unit for snapd-desktop-integration, revision 83...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.581663] loop4: detected capacity change from 0 to 187776
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.585010] systemd[1]: Mounting Mount unit for firefox, revision 3836 via mount-control...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.588029] systemd[1]: Starting Rule-based Manager for Device Events and Files...
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.589422] systemd[1]: Finished Apply Kernel Variables.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.598731] systemd[1]: Mounted Mount unit for bare, revision 5.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.601795] systemd[1]: Mounted Mount unit for core22, revision 1122.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.602010] systemd[1]: Mounted Mount unit for firefox, revision 3836.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.602168] systemd[1]: Mounted Mount unit for gnome-42-2204, revision 141.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.602314] systemd[1]: Mounted Mount unit for gtk-common-themes, revision 1535.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.602428] systemd[1]: Mounted Mount unit for firefox, revision 3836 via mount-control.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.602775] loop5: detected capacity change from 0 to 82800
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.603198] loop6: detected capacity change from 0 to 904
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.603423] loop7: detected capacity change from 0 to 25240
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.608618] systemd[1]: Mounted Mount unit for snap-store, revision 959.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.608753] systemd[1]: Mounted Mount unit for snapd, revision 20671.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.610211] systemd[1]: Mounted Mount unit for snapd-desktop-integration, revision 83.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.610250] systemd[1]: Reached target Mounted snaps.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.682799] systemd[1]: Started Journal Service.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.712360] systemd-journald[339]: Received client request to flush runtime journal.
Jun 30 05:38:40 ty-virtual-machine kernel: [    9.718098] systemd-journald[339]: File /var/log/journal/070005de4da9400ebf637e58010dc020/system.journal corrupted or uncleanly shut down, renaming and replacing.
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.508488] vmw_vmci 0000:00:07.7: MMIO register access is available
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.508786] vmw_vmci 0000:00:07.7: Using capabilities 0x3c
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.551398] Guest personality initialized and is active
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.551932] VMCI host device registered (name=vmci, major=10, minor=122)
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.551939] Initialized host personality
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.669463] vmwgfx 0000:00:0f.0: vgaarb: deactivate vga console
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.702688] Console: switching to colour dummy device 80x25
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728073] vmwgfx 0000:00:0f.0: [drm] FIFO at 0x00000000fe000000 size is 8192 kiB
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728222] vmwgfx 0000:00:0f.0: [drm] VRAM at 0x00000000e8000000 size is 131072 kiB
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728277] vmwgfx 0000:00:0f.0: [drm] Running on SVGA version 2.
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728302] vmwgfx 0000:00:0f.0: [drm] Capabilities: rect copy, cursor, cursor bypass, cursor bypass 2, 8bit emulation, alpha cursor, 3D, extended fifo, multimon, pitchlock, irq mask, display topology, gmr, traces, gmr2, screen object 2, command buffers, command buffers 2, gbobject, dx, hp cmd queue, no bb restriction, cap2 register, 
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728325] vmwgfx 0000:00:0f.0: [drm] Capabilities2: grow otable, intra surface copy, dx2, gb memsize 2, screendma reg, otable ptdepth2, non ms to ms stretchblt, cursor mob, mshint, cb max size 4mb, dx3, frame type, trace full fb, extra regs, lo staging, 
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728329] vmwgfx 0000:00:0f.0: [drm] DMA map mode: Caching DMA mappings.
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728673] vmwgfx 0000:00:0f.0: [drm] Legacy memory limits: VRAM = 4096 kB, FIFO = 256 kB, surface = 0 kB
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728678] vmwgfx 0000:00:0f.0: [drm] MOB limits: max mob size = 1048576 kB, max mob pages = 2097152
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728682] vmwgfx 0000:00:0f.0: [drm] Max GMR ids is 64
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728685] vmwgfx 0000:00:0f.0: [drm] Max number of GMR pages is 65536
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.728687] vmwgfx 0000:00:0f.0: [drm] Maximum display memory size is 262144 kiB
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.743614] vmwgfx 0000:00:0f.0: [drm] Screen Target display unit initialized
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.745031] vmwgfx 0000:00:0f.0: [drm] Fifo max 0x00040000 min 0x00001000 cap 0x0000077f
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.759605] vmwgfx 0000:00:0f.0: [drm] Using command buffers with DMA pool.
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.759621] vmwgfx 0000:00:0f.0: [drm] Available shader model: SM_5_1X.
Jun 30 05:38:40 ty-virtual-machine kernel: [   10.764089] [drm] Initialized vmwgfx 2.20.0 20211206 for 0000:00:0f.0 on minor 0
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.437722] fbcon: vmwgfxdrmfb (fb0) is primary device
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.440234] Console: switching to colour frame buffer device 160x50
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.452230] vmwgfx 0000:00:0f.0: [drm] fb0: vmwgfxdrmfb frame buffer device
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.626214] RAPL PMU: API unit is 2^-32 Joules, 0 fixed counters, 10737418240 ms ovfl timer
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.633121] cryptd: max_cpu_qlen set to 1000
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.655020] AVX2 version of gcm_enc/dec engaged.
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.657665] AES CTR mode by8 optimization enabled
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.806908] audit: type=1400 audit(1782812319.196:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=500 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.816275] audit: type=1400 audit(1782812319.208:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=501 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.816287] audit: type=1400 audit(1782812319.208:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=501 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.817448] audit: type=1400 audit(1782812319.208:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=512 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.817453] audit: type=1400 audit(1782812319.208:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=512 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.817455] audit: type=1400 audit(1782812319.208:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=512 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.821713] audit: type=1400 audit(1782812319.212:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oosplash" pid=515 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.824933] audit: type=1400 audit(1782812319.216:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="tcpdump" pid=514 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.832062] audit: type=1400 audit(1782812319.224:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=516 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.857581] audit: type=1400 audit(1782812319.248:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-xpdfimport" pid=520 comm="apparmor_parser"
Jun 30 05:38:40 ty-virtual-machine kernel: [   11.958432] intel_rapl_msr: PL4 support detected.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Condition check resulted in Manage Sound Card State (restore and store) being skipped.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Save/Restore Sound Card State...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting CUPS Scheduler...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting GRUB failed boot detection...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting OpenVPN service...
Jun 30 05:38:40 ty-virtual-machine accounts-daemon[712]: started daemon version 22.07.5
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Hostname Service...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting Permit User Sessions...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started LSB: automatic crash report generation.
Jun 30 05:38:40 ty-virtual-machine alsactl[820]: /usr/sbin/alsactl: load_state:1689: Cannot open /var/lib/alsa/asound.state for reading: No such file or directory
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished OpenVPN service.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: grub-initrd-fallback.service: Deactivated successfully.
Jun 30 05:38:40 ty-virtual-machine alsactl[820]: alsa-lib main.c:1412:(snd_use_case_mgr_open) error: failed to import hw:0 use case configuration -2
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished GRUB failed boot detection.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Permit User Sessions.
Jun 30 05:38:40 ty-virtual-machine udisksd[765]: failed to load module mdraid: libbd_mdraid.so.2: cannot open shared object file: No such file or directory
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Finished Save/Restore Sound Card State.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started User Login Management.
Jun 30 05:38:40 ty-virtual-machine ModemManager[799]: <info>  ModemManager (version 1.20.0) starting in system bus...
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Started Accounts Service.
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Reached target Sound Card.
Jun 30 05:38:40 ty-virtual-machine snapd-aa-prompt-listener[750]: AA Prompt listener not implemented
Jun 30 05:38:40 ty-virtual-machine systemd[1]: Starting GNOME Display Manager...
Jun 30 05:38:41 ty-virtual-machine udisksd[765]: Failed to load the 'mdraid' libblockdev plugin
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Starting Hold until boot process finishes up...
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started Unattended Upgrades Shutdown.
Jun 30 05:38:41 ty-virtual-machine systemd[1]: snapd.aa-prompt-listener.service: Deactivated successfully.
Jun 30 05:38:41 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started Hostname Service.
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.1483] hostname: hostname: using hostnamed
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.1484] hostname: static hostname changed from (none) to "ty-virtual-machine"
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.1534] dns-mgr[0x55960a86b2a0]: init: dns=systemd-resolved rc-manager=unmanaged (auto), plugin=systemd-resolved
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.1606] manager[0x55960a88e040]: rfkill: Wi-Fi hardware radio set enabled
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.1612] manager[0x55960a88e040]: rfkill: WWAN hardware radio set enabled
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2117] Loaded device plugin: NMTeamFactory (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-team.so)
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2238] Loaded device plugin: NMWwanFactory (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-wwan.so)
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2276] Loaded device plugin: NMAtmManager (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-adsl.so)
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2560] Loaded device plugin: NMWifiFactory (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-wifi.so)
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started Modem Manager.
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2799] Loaded device plugin: NMBluezManager (/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-bluetooth.so)
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2929] manager: rfkill: Wi-Fi enabled by radio killswitch; enabled by state file
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2942] manager: rfkill: WWAN enabled by radio killswitch; enabled by state file
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.2951] manager: Networking is enabled by state file
Jun 30 05:38:41 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3218] settings: Loaded settings plugin: ifupdown ("/usr/lib/x86_64-linux-gnu/NetworkManager/1.36.6/libnm-settings-plugin-ifupdown.so")
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3221] settings: Loaded settings plugin: keyfile (internal)
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3221] ifupdown: management mode: unmanaged
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3289] ifupdown: interfaces file /etc/network/interfaces doesn't exist
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started Disk Manager.
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3419] dhcp-init: Using DHCP client 'internal'
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3424] device (lo): carrier: link connected
Jun 30 05:38:41 ty-virtual-machine udisksd[765]: Acquired the name org.freedesktop.UDisks2 on the system message bus
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started GNOME Display Manager.
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3536] manager: (lo): new Generic device (/org/freedesktop/NetworkManager/Devices/1)
Jun 30 05:38:41 ty-virtual-machine udisksd[765]: Cleaning up mount point /media/ty/CDROM (device 11:0 is not mounted)
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3579] manager: (ens33): new Ethernet device (/org/freedesktop/NetworkManager/Devices/2)
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3636] settings: (ens33): created default wired connection 'Wired connection 1'
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.3647] device (ens33): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started CUPS Scheduler.
Jun 30 05:38:41 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.4058] failed to open /run/network/ifstate
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Received SIGRTMIN+21 from PID 408 (plymouthd).
Jun 30 05:38:41 ty-virtual-machine avahi-daemon[716]: Server startup complete. Host name is ty-virtual-machine.local. Local service cookie is 530715480.
Jun 30 05:38:41 ty-virtual-machine NetworkManager[721]: <info>  [1782812321.4512] modem-manager: ModemManager available
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]: No valid path found for iw
Jun 30 05:38:41 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.network1' unit='dbus-org.freedesktop.network1.service' requested by ':1.21' (uid=0 pid=864 comm="/usr/bin/networkctl list --no-pager --no-legend " label="unconfined")
Jun 30 05:38:41 ty-virtual-machine dbus-daemon[719]: [system] Activation via systemd failed for unit 'dbus-org.freedesktop.network1.service': Unit dbus-org.freedesktop.network1.service not found.
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Created slice User Slice of UID 128.
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[864]: WARNING: systemd-networkd is not running, output will be incomplete.
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]: ERROR:Unknown state for interface NetworkctlListState(idx=1, name='lo', type='loopback', operational='n/a', administrative='unmanaged'): n/a
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]: Traceback (most recent call last):
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:   File "/usr/bin/networkd-dispatcher", line 298, in trigger_all
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:     self.handle_state(iface_name,
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:   File "/usr/bin/networkd-dispatcher", line 348, in handle_state
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:     raise UnknownState(operational_state)
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]: UnknownState: n/a
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]: ERROR:Unknown state for interface NetworkctlListState(idx=2, name='ens33', type='ether', operational='n/a', administrative='unmanaged'): n/a
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]: Traceback (most recent call last):
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:   File "/usr/bin/networkd-dispatcher", line 298, in trigger_all
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:     self.handle_state(iface_name,
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:   File "/usr/bin/networkd-dispatcher", line 348, in handle_state
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]:     raise UnknownState(operational_state)
Jun 30 05:38:41 ty-virtual-machine networkd-dispatcher[736]: UnknownState: n/a
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Starting User Runtime Directory /run/user/128...
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Started Dispatcher daemon for systemd-networkd.
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Finished User Runtime Directory /run/user/128.
Jun 30 05:38:41 ty-virtual-machine systemd[1]: Starting User Manager for UID 128...
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Queued start job for default target Main User Target.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Created slice User Application Slice.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Created slice User Background Tasks Slice.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Created slice User Core Session Slice.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Started Pending report trigger for Ubuntu Report.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Reached target Paths.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Reached target Timers.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Starting D-Bus User Message Bus Socket...
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on GnuPG network certificate management daemon.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on GnuPG cryptographic agent and passphrase cache.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on PipeWire Multimedia System Socket.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on debconf communication socket.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on Sound System.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on REST API socket for snapd user session agent.
Jun 30 05:38:41 ty-virtual-machine systemd[867]: Listening on Speech Dispatcher Socket.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Listening on D-Bus User Message Bus Socket.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Reached target Sockets.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Reached target Basic System.
Jun 30 05:38:42 ty-virtual-machine systemd[1]: Started User Manager for UID 128.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Started PipeWire Multimedia Service.
Jun 30 05:38:42 ty-virtual-machine systemd[1]: Started Session c1 of User gdm.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Started PipeWire Media Session Manager.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Starting Sound Service...
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Started Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Starting Tracker metadata extractor...
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Started D-Bus User Message Bus.
Jun 30 05:38:42 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.RealtimeKit1' unit='rtkit-daemon.service' requested by ':1.26' (uid=128 pid=876 comm="/usr/bin/pipewire-media-session " label="unconfined")
Jun 30 05:38:42 ty-virtual-machine systemd[1]: Starting RealtimeKit Scheduling Policy Service...
Jun 30 05:38:42 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.RealtimeKit1'
Jun 30 05:38:42 ty-virtual-machine systemd[1]: Started RealtimeKit Scheduling Policy Service.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully called chroot.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully dropped privileges.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully limited resources.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Running.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 0 threads of 0 processes of 0 users.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Canary thread running.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Watchdog thread running.
Jun 30 05:38:42 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] AppArmor D-Bus mediation is enabled
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 874 of process 874 owned by '128' high priority at nice level -11.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 1 threads of 1 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 1 threads of 1 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 877 of process 877 owned by '128' high priority at nice level -11.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 2 threads of 2 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 893 of process 876 owned by '128' RT at priority 20.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 3 threads of 3 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 3 threads of 3 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.2' (uid=128 pid=880 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 3 threads of 3 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Starting Virtual filesystem service...
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 904 of process 874 owned by '128' RT at priority 20.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 4 threads of 3 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 30 05:38:42 ty-virtual-machine systemd[867]: Started Virtual filesystem service.
Jun 30 05:38:42 ty-virtual-machine gnome-session[894]: gnome-session-binary[894]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:38:42 ty-virtual-machine gnome-session[894]: gnome-session-binary[894]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:38:42 ty-virtual-machine gnome-session-binary[894]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:38:42 ty-virtual-machine gnome-session-binary[894]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 30 05:38:42 ty-virtual-machine pulseaudio[877]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 4 threads of 3 processes of 1 users.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 920 of process 877 owned by '128' RT at priority 5.
Jun 30 05:38:42 ty-virtual-machine rtkit-daemon[887]: Supervising 5 threads of 3 processes of 1 users.
Jun 30 05:38:43 ty-virtual-machine pulseaudio[877]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:38:43 ty-virtual-machine pulseaudio[877]: ALSA woke us up to write new data to the device, but there was actually nothing to write.
Jun 30 05:38:43 ty-virtual-machine pulseaudio[877]: Most likely this is a bug in the ALSA driver 'snd_ens1371'. Please report this issue to the ALSA developers.
Jun 30 05:38:43 ty-virtual-machine pulseaudio[877]: We were woken up with POLLOUT set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 30 05:38:43 ty-virtual-machine rtkit-daemon[887]: Supervising 5 threads of 3 processes of 1 users.
Jun 30 05:38:43 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 922 of process 877 owned by '128' RT at priority 5.
Jun 30 05:38:43 ty-virtual-machine rtkit-daemon[887]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:38:43 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.34' (uid=128 pid=877 comm="/usr/bin/pulseaudio --daemonize=no --log-target=jo" label="unconfined")
Jun 30 05:38:43 ty-virtual-machine systemd[1]: Condition check resulted in Bluetooth service being skipped.
Jun 30 05:38:43 ty-virtual-machine systemd[867]: Started Sound Service.
Jun 30 05:38:43 ty-virtual-machine gnome-shell[925]: Running GNOME Shell (using mutter 42.9) as a Wayland display server
Jun 30 05:38:43 ty-virtual-machine ModemManager[799]: <info>  [base-manager] couldn't check support for device '/sys/devices/pci0000:00/0000:00:11.0/0000:02:01.0': not supported by any plugin
Jun 30 05:38:44 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.2' (uid=128 pid=880 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:38:44 ty-virtual-machine gnome-shell[925]: Added device '/dev/dri/card0' (vmwgfx) using non-atomic mode setting.
Jun 30 05:38:44 ty-virtual-machine systemd[867]: Starting Tracker file system data miner...
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &DOCUMENTS. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &MUSIC. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &PICTURES. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &VIDEOS. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &DOWNLOAD. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &DOCUMENTS. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &MUSIC. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &PICTURES. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine tracker-miner-f[940]: Unable to get XDG user directory path for special directory &VIDEOS. Ignoring this location.
Jun 30 05:38:44 ty-virtual-machine snapd[752]: overlord.go:271: Acquiring state lock file
Jun 30 05:38:44 ty-virtual-machine snapd[752]: overlord.go:276: Acquired state lock file
Jun 30 05:38:44 ty-virtual-machine snapd[752]: daemon.go:247: started snapd/2.61.1 (series 16; classic) ubuntu/22.04 (amd64) linux/6.5.0-18-generic.
Jun 30 05:38:44 ty-virtual-machine kernel: [   17.328667] loop8: detected capacity change from 0 to 8
Jun 30 05:38:44 ty-virtual-machine systemd[1]: tmp-syscheck\x2dmountpoint\x2d3339106995.mount: Deactivated successfully.
Jun 30 05:38:44 ty-virtual-machine snapd[752]: daemon.go:340: adjusting startup timeout by 1m10s (pessimistic estimate of 30s plus 5s per snap)
Jun 30 05:38:44 ty-virtual-machine snapd[752]: backends.go:58: AppArmor status: apparmor is enabled and all features are available (using snapd provided apparmor_parser)
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.gtk.vfs.UDisks2VolumeMonitor' unit='gvfs-udisks2-volume-monitor.service' requested by ':1.8' (uid=128 pid=940 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Starting Virtual filesystem service - disk device monitor...
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gtk.vfs.UDisks2VolumeMonitor'
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Started Virtual filesystem service - disk device monitor.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.gtk.vfs.AfcVolumeMonitor' unit='gvfs-afc-volume-monitor.service' requested by ':1.8' (uid=128 pid=940 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Starting Virtual filesystem service - Apple File Conduit monitor...
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gtk.vfs.AfcVolumeMonitor'
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Started Virtual filesystem service - Apple File Conduit monitor.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.gtk.vfs.MTPVolumeMonitor' unit='gvfs-mtp-volume-monitor.service' requested by ':1.8' (uid=128 pid=940 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Starting Virtual filesystem service - Media Transfer Protocol monitor...
Jun 30 05:38:45 ty-virtual-machine systemd[1]: dmesg.service: Deactivated successfully.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gtk.vfs.MTPVolumeMonitor'
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Started Virtual filesystem service - Media Transfer Protocol monitor.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.gtk.vfs.GPhoto2VolumeMonitor' unit='gvfs-gphoto2-volume-monitor.service' requested by ':1.8' (uid=128 pid=940 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Starting Virtual filesystem service - digital camera monitor...
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.freedesktop.portal.Documents' unit='xdg-document-portal.service' requested by ':1.12' (uid=128 pid=879 comm="/usr/bin/snap run snapd-desktop-integration " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Starting flatpak document portal service...
Jun 30 05:38:45 ty-virtual-machine systemd[1]: Started Snap Daemon.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine systemd[1]: Starting Wait until snapd is fully seeded...
Jun 30 05:38:45 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gtk.vfs.GPhoto2VolumeMonitor'
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Started Virtual filesystem service - digital camera monitor.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.gtk.vfs.GoaVolumeMonitor' unit='gvfs-goa-volume-monitor.service' requested by ':1.8' (uid=128 pid=940 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating via systemd: service name='org.freedesktop.impl.portal.PermissionStore' unit='xdg-permission-store.service' requested by ':1.14' (uid=128 pid=1022 comm="/usr/libexec/xdg-document-portal " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Starting Virtual filesystem service - GNOME Online Accounts monitor...
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Starting sandboxed app permission store...
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Started sandboxed app permission store.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.freedesktop.portal.Documents'
Jun 30 05:38:45 ty-virtual-machine systemd[867]: Started flatpak document portal service.
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating service name='org.gnome.OnlineAccounts' requested by ':1.16' (uid=128 pid=1032 comm="/usr/libexec/gvfs-goa-volume-monitor " label="unconfined")
Jun 30 05:38:45 ty-virtual-machine kernel: [   18.218660] kauditd_printk_skb: 36 callbacks suppressed
Jun 30 05:38:45 ty-virtual-machine kernel: [   18.218667] audit: type=1400 audit(1782812325.608:48): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=879 comm="snap-confine" capability=12  capname="net_admin"
Jun 30 05:38:45 ty-virtual-machine kernel: [   18.218698] audit: type=1400 audit(1782812325.608:49): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=879 comm="snap-confine" capability=38  capname="perfmon"
Jun 30 05:38:45 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:38:45 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:38:45 ty-virtual-machine gnome-shell[925]: Created gbm renderer for '/dev/dri/card0'
Jun 30 05:38:45 ty-virtual-machine gnome-shell[925]: Boot VGA GPU /dev/dri/card0 selected as primary
Jun 30 05:38:45 ty-virtual-machine systemd[1]: Finished Wait until snapd is fully seeded.
Jun 30 05:38:45 ty-virtual-machine systemd[1]: Condition check resulted in Auto import assertions from block devices being skipped.
Jun 30 05:38:45 ty-virtual-machine systemd[1]: tmp-snap.rootfs_JVNHlC.mount: Deactivated successfully.
Jun 30 05:38:45 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.a11y.Bus' requested by ':1.4' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:46 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Successfully activated service 'org.a11y.Bus'
Jun 30 05:38:46 ty-virtual-machine goa-daemon[1046]: goa-daemon version 3.44.0 starting
Jun 30 05:38:46 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Activating service name='org.gnome.Identity' requested by ':1.17' (uid=128 pid=1046 comm="/usr/libexec/goa-daemon " label="unconfined")
Jun 30 05:38:46 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gnome.OnlineAccounts'
Jun 30 05:38:46 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gtk.vfs.GoaVolumeMonitor'
Jun 30 05:38:46 ty-virtual-machine systemd[867]: Started Virtual filesystem service - GNOME Online Accounts monitor.
Jun 30 05:38:46 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.UPower' unit='upower.service' requested by ':1.40' (uid=128 pid=940 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:38:46 ty-virtual-machine systemd[1]: Starting Daemon for power management...
Jun 30 05:38:46 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.gnome.Identity'
Jun 30 05:38:46 ty-virtual-machine gnome-shell[925]: Using public X11 display :1024, (using :1025 for managed services)
Jun 30 05:38:46 ty-virtual-machine gnome-shell[925]: Using Wayland display name 'wayland-0'
Jun 30 05:38:46 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.UPower'
Jun 30 05:38:46 ty-virtual-machine systemd[1]: Started Daemon for power management.
Jun 30 05:38:46 ty-virtual-machine org.gnome.Shell.desktop[1094]: (WW) Option "-listen" for file descriptors is deprecated
Jun 30 05:38:46 ty-virtual-machine org.gnome.Shell.desktop[1094]: Please use "-listenfd" instead.
Jun 30 05:38:46 ty-virtual-machine org.gnome.Shell.desktop[1094]: (WW) Option "-listen" for file descriptors is deprecated
Jun 30 05:38:46 ty-virtual-machine org.gnome.Shell.desktop[1094]: Please use "-listenfd" instead.
Jun 30 05:38:46 ty-virtual-machine snapd-desktop-integration.snapd-desktop-integration[879]: Sorry, home directories outside of /home needs configuration.
Jun 30 05:38:46 ty-virtual-machine snapd-desktop-integration.snapd-desktop-integration[879]: See https://forum.snapcraft.io/t/11209 for details.
Jun 30 05:38:46 ty-virtual-machine systemd[867]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Main process exited, code=exited, status=1/FAILURE
Jun 30 05:38:46 ty-virtual-machine systemd[867]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Failed with result 'exit-code'.
Jun 30 05:38:46 ty-virtual-machine systemd[867]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Consumed 3.185s CPU time.
Jun 30 05:38:47 ty-virtual-machine dbus-daemon[886]: [session uid=128 pid=886] Successfully activated service 'org.freedesktop.Tracker3.Miner.Files'
Jun 30 05:38:47 ty-virtual-machine systemd[867]: Started Tracker file system data miner.
Jun 30 05:38:47 ty-virtual-machine systemd[867]: Started Tracker metadata extractor.
Jun 30 05:38:47 ty-virtual-machine systemd[867]: Reached target Main User Target.
Jun 30 05:38:47 ty-virtual-machine systemd[867]: Startup finished in 5.415s.
Jun 30 05:38:47 ty-virtual-machine gnome-shell[925]: Unset XDG_SESSION_ID, getCurrentSessionProxy() called outside a user session. Asking logind directly.
Jun 30 05:38:47 ty-virtual-machine gnome-shell[925]: Will monitor session c1
Jun 30 05:38:47 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.locale1' unit='dbus-org.freedesktop.locale1.service' requested by ':1.35' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Starting Locale Service...
Jun 30 05:38:47 ty-virtual-machine NetworkManager[721]: <info>  [1782812327.3997] manager: startup complete
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Finished Network Manager Wait Online.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Reached target Network is Online.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started Download data for packages that failed at package install time.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started Check to see whether there is a new version of Ubuntu available.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Reached target Timer Units.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started Make remote CUPS printers available locally.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Starting Tool to automatically collect and submit kernel crash signatures...
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Condition check resulted in Ubuntu Pro Background Auto Attach being skipped.
Jun 30 05:38:47 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.locale1'
Jun 30 05:38:47 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.freedesktop.impl.portal.PermissionStore' requested by ':1.3' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started crash report submission.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started Locale Service.
Jun 30 05:38:47 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 30 05:38:47 ty-virtual-machine systemd[1]: kerneloops.service: Found left-over process 1114 (kerneloops) in control group while starting unit. Ignoring.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Jun 30 05:38:47 ty-virtual-machine whoopsie[1108]: [05:38:47] Using lock path: /var/lock/whoopsie/lock
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started Tool to automatically collect and submit kernel crash signatures.
Jun 30 05:38:47 ty-virtual-machine systemd[1]: whoopsie.service: Deactivated successfully.
Jun 30 05:38:47 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.GeoClue2' unit='geoclue.service' requested by ':1.35' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Starting Location Lookup Service...
Jun 30 05:38:47 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.PackageKit' unit='packagekit.service' requested by ':1.35' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Starting PackageKit Daemon...
Jun 30 05:38:47 ty-virtual-machine gnome-shell[925]: Extension ding@rastersoft.com already installed in /usr/share/gnome-shell/extensions/ding@rastersoft.com. /usr/share/gnome-shell/extensions/ding@rastersoft.com will not be loaded
Jun 30 05:38:47 ty-virtual-machine gnome-shell[925]: Extension ubuntu-appindicators@ubuntu.com already installed in /usr/share/gnome-shell/extensions/ubuntu-appindicators@ubuntu.com. /usr/share/gnome-shell/extensions/ubuntu-appindicators@ubuntu.com will not be loaded
Jun 30 05:38:47 ty-virtual-machine gnome-shell[925]: Extension ubuntu-dock@ubuntu.com already installed in /usr/share/gnome-shell/extensions/ubuntu-dock@ubuntu.com. /usr/share/gnome-shell/extensions/ubuntu-dock@ubuntu.com will not be loaded
Jun 30 05:38:47 ty-virtual-machine PackageKit: daemon start
Jun 30 05:38:47 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.gnome.Shell.Notifications' requested by ':1.3' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:47 ty-virtual-machine /usr/libexec/gdm-wayland-session[1068]: dbus-daemon[1068]: Activating service name='org.a11y.atspi.Registry' requested by ':1.0' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:47 ty-virtual-machine /usr/libexec/gdm-wayland-session[1068]: dbus-daemon[1068]: Successfully activated service 'org.a11y.atspi.Registry'
Jun 30 05:38:47 ty-virtual-machine /usr/libexec/gdm-wayland-session[1129]: SpiRegistry daemon is running with well-known name - org.a11y.atspi.Registry
Jun 30 05:38:47 ty-virtual-machine org.gnome.Shell.desktop[925]: Window manager warning: Failed to parse saved session file: Failed to open file “/var/lib/gdm3/.config/mutter/sessions/1028480f64940ad052178281232325135500000008940000.ms”: No such file or directory
Jun 30 05:38:47 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.GeoClue2'
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started Location Lookup Service.
Jun 30 05:38:47 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.PackageKit'
Jun 30 05:38:47 ty-virtual-machine systemd[1]: Started PackageKit Daemon.
Jun 30 05:38:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Successfully activated service 'org.gnome.Shell.Notifications'
Jun 30 05:38:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.gtk.vfs.Daemon' requested by ':1.18' (uid=128 pid=1153 comm="ibus-daemon --panel disable " label="unconfined")
Jun 30 05:38:48 ty-virtual-machine gnome-shell[925]: JS ERROR: TypeError: this._managerProxy is undefined#012_onGeoclueVanished@resource:///org/gnome/shell/ui/status/location.js:169:9
Jun 30 05:38:48 ty-virtual-machine kernel: [   20.764707] rfkill: input handler disabled
Jun 30 05:38:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.freedesktop.systemd1' requested by ':1.9' (uid=128 pid=1142 comm="/usr/libexec/gsd-sharing " label="unconfined")
Jun 30 05:38:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activated service 'org.freedesktop.systemd1' failed: Process org.freedesktop.systemd1 exited with status 1
Jun 30 05:38:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 30 05:38:48 ty-virtual-machine gsd-sharing[1142]: Failed to StopUnit service: GDBus.Error:org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
Jun 30 05:38:48 ty-virtual-machine gsd-sharing[1142]: Failed to StopUnit service: GDBus.Error:org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
Jun 30 05:38:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.freedesktop.portal.IBus' requested by ':1.18' (uid=128 pid=1153 comm="ibus-daemon --panel disable " label="unconfined")
Jun 30 05:38:48 ty-virtual-machine NetworkManager[721]: <info>  [1782812328.3257] agent-manager: agent[445a15a733e60bf5,:1.35/org.gnome.Shell.NetworkAgent/128]: agent registered
Jun 30 05:38:48 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 30 05:38:48 ty-virtual-machine gnome-shell[925]: Error looking up permission: GDBus.Error:org.freedesktop.portal.Error.NotFound: No entry for geolocation
Jun 30 05:38:49 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.35' (uid=128 pid=925 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:38:49 ty-virtual-machine systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 30 05:38:49 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 30 05:38:49 ty-virtual-machine systemd[1]: Started Fingerprint Authentication Daemon.
Jun 30 05:38:49 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.ColorManager' unit='colord.service' requested by ':1.58' (uid=128 pid=1148 comm="/usr/libexec/gsd-color " label="unconfined")
Jun 30 05:38:49 ty-virtual-machine systemd[1]: Starting Manage, Install and Generate Color Profiles...
Jun 30 05:38:49 ty-virtual-machine colord[1277]: failed to get edid data: EDID length is too small
Jun 30 05:38:49 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.ColorManager'
Jun 30 05:38:49 ty-virtual-machine systemd[1]: Started Manage, Install and Generate Color Profiles.
Jun 30 05:38:49 ty-virtual-machine gnome-shell[925]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available#012asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 30 05:38:49 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.gnome.ScreenSaver' requested by ':1.22' (uid=128 pid=1191 comm="/usr/libexec/gsd-power " label="unconfined")
Jun 30 05:38:49 ty-virtual-machine spice-vdagent[1283]: vdagent virtio channel /dev/virtio-ports/com.redhat.spice.0 does not exist, exiting
Jun 30 05:38:49 ty-virtual-machine gsd-media-keys[1172]: Failed to grab accelerator for keybinding settings:hibernate
Jun 30 05:38:49 ty-virtual-machine gsd-media-keys[1172]: Failed to grab accelerator for keybinding settings:playback-repeat
Jun 30 05:38:49 ty-virtual-machine gnome-session-binary[894]: Entering running state
Jun 30 05:38:49 ty-virtual-machine xbrlapi.desktop[1288]: openConnection: connect: No such file or directory
Jun 30 05:38:49 ty-virtual-machine xbrlapi.desktop[1288]: cannot connect to braille devices daemon brltty at :0
Jun 30 05:38:49 ty-virtual-machine gnome-shell[925]: ATK Bridge is disabled but a11y has already been enabled.
Jun 30 05:38:50 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Successfully activated service 'org.gnome.ScreenSaver'
Jun 30 05:38:50 ty-virtual-machine gsd-color[1148]: failed to get edid: unable to get EDID for output
Jun 30 05:38:50 ty-virtual-machine ibus-daemon[1153]: GChildWatchSource: Exit status of a child process was requested but ECHILD was received by waitpid(). See the documentation of g_child_watch_source_new() for possible causes.
Jun 30 05:38:50 ty-virtual-machine gsd-color[1148]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:38:50 ty-virtual-machine org.gnome.Shell.desktop[1311]: The XKEYBOARD keymap compiler (xkbcomp) reports:
Jun 30 05:38:50 ty-virtual-machine org.gnome.Shell.desktop[1311]: > Warning:          Unsupported maximum keycode 708, clipping.
Jun 30 05:38:50 ty-virtual-machine org.gnome.Shell.desktop[1311]: >                   X11 cannot support keycodes above 255.
Jun 30 05:38:50 ty-virtual-machine org.gnome.Shell.desktop[1311]: Errors from xkbcomp are not fatal to the X server
Jun 30 05:38:50 ty-virtual-machine gnome-shell[925]: Registering session with GDM
Jun 30 05:38:50 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Activating service name='org.freedesktop.portal.IBus' requested by ':1.36' (uid=128 pid=1304 comm="ibus-daemon --panel disable -r --xim " label="unconfined")
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Received SIGRTMIN+21 from PID 408 (plymouthd).
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Finished Hold until boot process finishes up.
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Reached target Multi-User System.
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Reached target Graphical Interface.
Jun 30 05:38:50 ty-virtual-machine /usr/libexec/gdm-wayland-session[892]: dbus-daemon[892]: [session uid=128 pid=892] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Starting Set console scheme...
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Starting Record Runlevel Change in UTMP...
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Finished Set console scheme.
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Created slice Slice /system/getty.
Jun 30 05:38:50 ty-virtual-machine systemd[1]: systemd-update-utmp-runlevel.service: Deactivated successfully.
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Finished Record Runlevel Change in UTMP.
Jun 30 05:38:50 ty-virtual-machine systemd[1]: Startup finished in 8.844s (kernel) + 14.288s (userspace) = 23.133s.
Jun 30 05:38:51 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 05:39:07 ty-virtual-machine systemd[1]: Created slice User Slice of UID 1000.
Jun 30 05:39:07 ty-virtual-machine systemd[1]: Starting User Runtime Directory /run/user/1000...
Jun 30 05:39:07 ty-virtual-machine systemd[1]: Finished User Runtime Directory /run/user/1000.
Jun 30 05:39:07 ty-virtual-machine systemd[1]: Starting User Manager for UID 1000...
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Queued start job for default target Main User Target.
Jun 30 05:39:08 ty-virtual-machine kernel: [   40.810436] systemd-journald[339]: File /var/log/journal/070005de4da9400ebf637e58010dc020/user-1000.journal corrupted or uncleanly shut down, renaming and replacing.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Created slice User Application Slice.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Created slice User Background Tasks Slice.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Created slice User Core Session Slice.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started Pending report trigger for Ubuntu Report.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Reached target Paths.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Reached target Timers.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Starting D-Bus User Message Bus Socket...
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on GnuPG network certificate management daemon.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on GnuPG cryptographic agent and passphrase cache.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on PipeWire Multimedia System Socket.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on debconf communication socket.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on Sound System.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on REST API socket for snapd user session agent.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on Speech Dispatcher Socket.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Listening on D-Bus User Message Bus Socket.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Reached target Sockets.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Reached target Basic System.
Jun 30 05:39:08 ty-virtual-machine systemd[1]: Started User Manager for UID 1000.
Jun 30 05:39:08 ty-virtual-machine systemd[1]: Started Session 2 of User ty.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started PipeWire Multimedia Service.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started PipeWire Media Session Manager.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Starting Sound Service...
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Starting Tracker metadata extractor...
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started Ubuntu report sends pending metrics data.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 1357 of process 1357 owned by '1000' high priority at nice level -11.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 2 users.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: message repeated 2 times: [ Supervising 7 threads of 4 processes of 2 users.]
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started D-Bus User Message Bus.
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] AppArmor D-Bus mediation is enabled
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating systemd to hand-off: service name='org.freedesktop.portal.Documents' unit='xdg-document-portal.service' requested by ':1.1' (uid=1000 pid=1360 comm="/usr/bin/snap run snapd-desktop-integration " label="unconfined")
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.systemd1'
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Starting flatpak document portal service...
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.3' (uid=1000 pid=1361 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Starting Virtual filesystem service...
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.freedesktop.impl.portal.PermissionStore' unit='xdg-permission-store.service' requested by ':1.4' (uid=1000 pid=1393 comm="/usr/libexec/xdg-document-portal " label="unconfined")
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Starting sandboxed app permission store...
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started Virtual filesystem service.
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started sandboxed app permission store.
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.portal.Documents'
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Started flatpak document portal service.
Jun 30 05:39:08 ty-virtual-machine kernel: [   41.150445] audit: type=1400 audit(1782812348.540:50): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=1360 comm="snap-confine" capability=12  capname="net_admin"
Jun 30 05:39:08 ty-virtual-machine kernel: [   41.150461] audit: type=1400 audit(1782812348.540:51): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=1360 comm="snap-confine" capability=38  capname="perfmon"
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 1368 of process 1358 owned by '1000' RT at priority 20.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Supervising 8 threads of 5 processes of 2 users.
Jun 30 05:39:08 ty-virtual-machine kernel: [   41.174473] workqueue: pcpu_balance_workfn hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 1359 of process 1359 owned by '1000' high priority at nice level -11.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Supervising 9 threads of 6 processes of 2 users.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Supervising 9 threads of 6 processes of 2 users.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 1390 of process 1357 owned by '1000' RT at priority 20.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Supervising 10 threads of 6 processes of 2 users.
Jun 30 05:39:08 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 30s"
Jun 30 05:39:08 ty-virtual-machine kernel: [   41.290195] rfkill: input handler enabled
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Files' unit='tracker-miner-fs-3.service' requested by ':1.3' (uid=1000 pid=1361 comm="/usr/libexec/tracker-extract-3 " label="unconfined")
Jun 30 05:39:08 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.76' (uid=1000 pid=1359 comm="/usr/bin/pulseaudio --daemonize=no --log-target=jo" label="unconfined")
Jun 30 05:39:08 ty-virtual-machine systemd[1]: Condition check resulted in Bluetooth service being skipped.
Jun 30 05:39:08 ty-virtual-machine rtkit-daemon[887]: Supervising 10 threads of 6 processes of 2 users.
Jun 30 05:39:08 ty-virtual-machine systemd[1350]: Starting Tracker file system data miner...
Jun 30 05:39:08 ty-virtual-machine systemd[1]: systemd-fsckd.service: Deactivated successfully.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Created slice Slice /app/gnome-session-manager.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Path trigger for Apport crash notifications.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Path trigger for new release of Ubuntu notifications.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Reached target GNOME Wayland Session.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Reached target GNOME Shell.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Condition check resulted in GNOME Initial Setup Copy Worker being skipped.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Start gnome-keyring as SSH agent...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Start gnome-keyring for the Secrets Service, and PKCS #11...
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gtk.vfs.UDisks2VolumeMonitor' unit='gvfs-udisks2-volume-monitor.service' requested by ':1.10' (uid=1000 pid=1439 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Monitor Session leader for GNOME Session...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Session Migration...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Rewrite dynamic launcher portal entries...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Monitor Session leader for GNOME Session.
Jun 30 05:39:09 ty-virtual-machine sh[1491]: dbus-update-activation-environment: setting SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:39:09 ty-virtual-machine sh[1491]: dbus-update-activation-environment: setting SSH_AGENT_LAUNCHER=gnome-keyring
Jun 30 05:39:09 ty-virtual-machine gnome-keyring-daemon[1492]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Virtual filesystem service - disk device monitor...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Finished Start gnome-keyring for the Secrets Service, and PKCS #11.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Finished Session Migration.
Jun 30 05:39:09 ty-virtual-machine sh[1482]: /bin/sh: 1: initctl: not found
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Finished Start gnome-keyring as SSH agent.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Finished Rewrite dynamic launcher portal entries.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started OpenSSH Agent.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Reached target Session services which should run early before the graphical session is brought up.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Reached target Tasks to be run before GNOME Session starts.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting GNOME Session Manager (session: ubuntu)...
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gtk.vfs.UDisks2VolumeMonitor'
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Virtual filesystem service - disk device monitor.
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gtk.vfs.AfcVolumeMonitor' unit='gvfs-afc-volume-monitor.service' requested by ':1.10' (uid=1000 pid=1439 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Virtual filesystem service - Apple File Conduit monitor...
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gtk.vfs.AfcVolumeMonitor'
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Virtual filesystem service - Apple File Conduit monitor.
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gtk.vfs.MTPVolumeMonitor' unit='gvfs-mtp-volume-monitor.service' requested by ':1.10' (uid=1000 pid=1439 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Virtual filesystem service - Media Transfer Protocol monitor...
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gtk.vfs.MTPVolumeMonitor'
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Virtual filesystem service - Media Transfer Protocol monitor.
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gtk.vfs.GPhoto2VolumeMonitor' unit='gvfs-gphoto2-volume-monitor.service' requested by ':1.10' (uid=1000 pid=1439 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Virtual filesystem service - digital camera monitor...
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gtk.vfs.GPhoto2VolumeMonitor'
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Virtual filesystem service - digital camera monitor.
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gtk.vfs.GoaVolumeMonitor' unit='gvfs-goa-volume-monitor.service' requested by ':1.10' (uid=1000 pid=1439 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:39:09 ty-virtual-machine gnome-keyring-pkcs11.desktop[1526]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting Virtual filesystem service - GNOME Online Accounts monitor...
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.gnome.OnlineAccounts' requested by ':1.30' (uid=1000 pid=1525 comm="/usr/libexec/gvfs-goa-volume-monitor " label="unconfined")
Jun 30 05:39:09 ty-virtual-machine gnome-session[1500]: gnome-session-binary[1500]: GnomeDesktop-WARNING: Could not create transient scope for PID 1522: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1522 does not exist.
Jun 30 05:39:09 ty-virtual-machine gnome-session-binary[1500]: GnomeDesktop-WARNING: Could not create transient scope for PID 1522: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1522 does not exist.
Jun 30 05:39:09 ty-virtual-machine gnome-keyring-ssh.desktop[1530]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:09 ty-virtual-machine gnome-keyring-secrets.desktop[1533]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started GNOME Session Manager (session: ubuntu).
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Reached target GNOME Session Manager is ready.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting GNOME Shell on Wayland...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting GNOME Shell on X11...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 1.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Stopped GNOME Shell on X11.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting GNOME Shell on X11...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 2.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Stopped GNOME Shell on X11.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Starting GNOME Shell on X11...
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 3.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Stopped GNOME Shell on X11.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Start request repeated too quickly.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started GNOME Shell on X11.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:09 ty-virtual-machine goa-daemon[1532]: goa-daemon version 3.44.0 starting
Jun 30 05:39:09 ty-virtual-machine gnome-shell[1543]: Running GNOME Shell (using mutter 42.9) as a Wayland display server
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.gnome.Identity' requested by ':1.32' (uid=1000 pid=1532 comm="/usr/libexec/goa-daemon " label="unconfined")
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.OnlineAccounts'
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gtk.vfs.GoaVolumeMonitor'
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Virtual filesystem service - GNOME Online Accounts monitor.
Jun 30 05:39:09 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 1440 of process 1359 owned by '1000' RT at priority 5.
Jun 30 05:39:09 ty-virtual-machine rtkit-daemon[887]: Supervising 11 threads of 6 processes of 2 users.
Jun 30 05:39:09 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.Identity'
Jun 30 05:39:09 ty-virtual-machine gnome-shell[1543]: Added device '/dev/dri/card0' (vmwgfx) using non-atomic mode setting.
Jun 30 05:39:09 ty-virtual-machine systemd[1350]: Started Sound Service.
Jun 30 05:39:09 ty-virtual-machine pulseaudio[1359]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:39:10 ty-virtual-machine rtkit-daemon[887]: Supervising 11 threads of 6 processes of 2 users.
Jun 30 05:39:10 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 1578 of process 1359 owned by '1000' RT at priority 5.
Jun 30 05:39:10 ty-virtual-machine rtkit-daemon[887]: Supervising 12 threads of 6 processes of 2 users.
Jun 30 05:39:10 ty-virtual-machine pulseaudio[1359]: Disabling timer-based scheduling because running inside a VM.
Jun 30 05:39:10 ty-virtual-machine pulseaudio[1359]: ALSA woke us up to write new data to the device, but there was actually nothing to write.
Jun 30 05:39:10 ty-virtual-machine pulseaudio[1359]: Most likely this is a bug in the ALSA driver 'snd_ens1371'. Please report this issue to the ALSA developers.
Jun 30 05:39:10 ty-virtual-machine pulseaudio[1359]: We were woken up with POLLOUT set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 30 05:39:10 ty-virtual-machine rtkit-daemon[887]: Supervising 12 threads of 6 processes of 2 users.
Jun 30 05:39:10 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 1583 of process 1359 owned by '1000' RT at priority 5.
Jun 30 05:39:10 ty-virtual-machine rtkit-daemon[887]: Supervising 13 threads of 6 processes of 2 users.
Jun 30 05:39:10 ty-virtual-machine gnome-shell[1543]: Created gbm renderer for '/dev/dri/card0'
Jun 30 05:39:10 ty-virtual-machine gnome-shell[1543]: Boot VGA GPU /dev/dri/card0 selected as primary
Jun 30 05:39:10 ty-virtual-machine gnome-shell[1543]: Using public X11 display :0, (using :1 for managed services)
Jun 30 05:39:10 ty-virtual-machine gnome-shell[1543]: Using Wayland display name 'wayland-0'
Jun 30 05:39:11 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.Tracker3.Miner.Files'
Jun 30 05:39:11 ty-virtual-machine systemd[1350]: Started Tracker file system data miner.
Jun 30 05:39:11 ty-virtual-machine systemd[1350]: Started Tracker metadata extractor.
Jun 30 05:39:11 ty-virtual-machine systemd[1350]: Reached target Main User Target.
Jun 30 05:39:11 ty-virtual-machine gnome-shell[1543]: Unset XDG_SESSION_ID, getCurrentSessionProxy() called outside a user session. Asking logind directly.
Jun 30 05:39:11 ty-virtual-machine gnome-shell[1543]: Will monitor session 2
Jun 30 05:39:12 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.gnome.Shell.CalendarServer' requested by ':1.34' (uid=1000 pid=1543 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:39:12 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gnome.evolution.dataserver.Sources5' unit='evolution-source-registry.service' requested by ':1.37' (uid=1000 pid=1623 comm="/usr/libexec/gnome-shell-calendar-server " label="unconfined")
Jun 30 05:39:12 ty-virtual-machine systemd[1350]: Starting Evolution source registry...
Jun 30 05:39:12 ty-virtual-machine snapd-desktop-i[1628]: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Jun 30 05:39:12 ty-virtual-machine snapd-desktop-i[1628]: Failed to do gtk init. Waiting for a new session with desktop capabilities.
Jun 30 05:39:12 ty-virtual-machine snapd-desktop-i[1628]: Checking session /org/freedesktop/login1/session/c1...
Jun 30 05:39:12 ty-virtual-machine gnome-shell[1543]: Telepathy is not available, chat integration will be disabled.
Jun 30 05:39:12 ty-virtual-machine snapd-desktop-i[1628]: Checking session /org/freedesktop/login1/session/_32...
Jun 30 05:39:12 ty-virtual-machine snapd-desktop-i[1628]: Is a desktop session! Forcing a reload.
Jun 30 05:39:12 ty-virtual-machine snapd-desktop-i[1628]: Loop exited. Forcing reload.
Jun 30 05:39:12 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.evolution.dataserver.Sources5'
Jun 30 05:39:12 ty-virtual-machine systemd[1350]: Started Evolution source registry.
Jun 30 05:39:12 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.Shell.CalendarServer'
Jun 30 05:39:12 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gnome.evolution.dataserver.Calendar8' unit='evolution-calendar-factory.service' requested by ':1.37' (uid=1000 pid=1623 comm="/usr/libexec/gnome-shell-calendar-server " label="unconfined")
Jun 30 05:39:12 ty-virtual-machine systemd[1350]: Starting Evolution calendar service...
Jun 30 05:39:12 ty-virtual-machine systemd[1350]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Consumed 2.700s CPU time.
Jun 30 05:39:12 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.evolution.dataserver.Calendar8'
Jun 30 05:39:12 ty-virtual-machine systemd[1350]: Started Evolution calendar service.
Jun 30 05:39:12 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='ca.desrt.dconf' unit='dconf.service' requested by ':1.39' (uid=1000 pid=1642 comm="/usr/libexec/evolution-calendar-factory " label="unconfined")
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gnome.evolution.dataserver.AddressBook10' unit='evolution-addressbook-factory.service' requested by ':1.39' (uid=1000 pid=1642 comm="/usr/libexec/evolution-calendar-factory " label="unconfined")
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting User preferences database...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting Evolution address book service...
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'ca.desrt.dconf'
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Started User preferences database.
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gtk.vfs.Metadata' unit='gvfs-metadata.service' requested by ':1.39' (uid=1000 pid=1642 comm="/usr/libexec/evolution-calendar-factory " label="unconfined")
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting Virtual filesystem metadata service...
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gtk.vfs.Metadata'
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Started Virtual filesystem metadata service.
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.evolution.dataserver.AddressBook10'
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Started Evolution address book service.
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.freedesktop.FileManager1' requested by ':1.34' (uid=1000 pid=1543 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.gnome.Shell.Notifications' requested by ':1.34' (uid=1000 pid=1543 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:39:13 ty-virtual-machine at-spi-dbus-bus.desktop[1546]: dbus-daemon[1546]: Activating service name='org.a11y.atspi.Registry' requested by ':1.0' (uid=1000 pid=1543 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 30 05:39:13 ty-virtual-machine at-spi-dbus-bus.desktop[1546]: dbus-daemon[1546]: Successfully activated service 'org.a11y.atspi.Registry'
Jun 30 05:39:13 ty-virtual-machine at-spi-dbus-bus.desktop[1685]: SpiRegistry daemon is running with well-known name - org.a11y.atspi.Registry
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Started GNOME Shell on Wayland.
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Reached target GNOME Session is initialized.
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: GNOME session X11 services is inactive.
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Dependency failed for GNOME XSettings service.
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: org.gnome.SettingsDaemon.XSettings.service: Job org.gnome.SettingsDaemon.XSettings.service/start failed with result 'dependency'.
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: gnome-session-x11-services-ready.target: Job gnome-session-x11-services-ready.target/verify-active failed with result 'dependency'.
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Reached target GNOME Session (session: ubuntu).
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Reached target GNOME XSettings target.
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting Signal initialization done to GNOME Session Manager...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting IBus Daemon for GNOME...
Jun 30 05:39:13 ty-virtual-machine kernel: [   46.230524] workqueue: pcpu_balance_workfn hogged CPU for >10000us 8 times, consider switching to WQ_UNBOUND
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME accessibility service...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME color management service...
Jun 30 05:39:13 ty-virtual-machine kernel: [   46.273778] ISO 9660 Extensions: Microsoft Joliet Level 3
Jun 30 05:39:13 ty-virtual-machine kernel: [   46.299336] ISO 9660 Extensions: RRIP_1991A
Jun 30 05:39:13 ty-virtual-machine udisksd[765]: Mounted /dev/sr1 at /media/ty/Ubuntu 22.04.4 LTS amd64 on behalf of uid 1000
Jun 30 05:39:13 ty-virtual-machine udisksd[765]: Mounted /dev/sr0 at /media/ty/CDROM on behalf of uid 1000
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME date & time service...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME maintenance of expirable data service...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME keyboard configuration service...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME keyboard shortcuts service...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME power management service...
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME printer notifications service...
Jun 30 05:39:13 ty-virtual-machine gnome-shell[1543]: Error looking up permission: GDBus.Error:org.freedesktop.portal.Error.NotFound: No entry for geolocation
Jun 30 05:39:13 ty-virtual-machine systemd[1350]: Starting GNOME RFKill support service...
Jun 30 05:39:13 ty-virtual-machine spice-vdagent[1713]: vdagent virtio channel /dev/virtio-ports/com.redhat.spice.0 does not exist, exiting
Jun 30 05:39:13 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.Shell.Notifications'
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Starting GNOME FreeDesktop screensaver service...
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Starting GNOME file sharing service...
Jun 30 05:39:14 ty-virtual-machine NetworkManager[721]: <info>  [1782812354.0522] agent-manager: agent[3a365232f1a4df4e,:1.82/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Starting GNOME smartcard service...
Jun 30 05:39:14 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.freedesktop.portal.IBus' requested by ':1.54' (uid=1000 pid=1709 comm="/usr/bin/ibus-daemon --panel disable " label="unconfined")
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Starting GNOME sound sample caching service...
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Starting GNOME Wacom tablet support service...
Jun 30 05:39:14 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Finished Signal initialization done to GNOME Session Manager.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME accessibility service.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME maintenance of expirable data service.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME date & time service.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started IBus Daemon for GNOME.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME accessibility target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME date & time target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME maintenance of expirable data target.
Jun 30 05:39:14 ty-virtual-machine gnome-session-binary[1500]: Entering running state
Jun 30 05:39:14 ty-virtual-machine gnome-session[1500]: gnome-session-binary[1500]: GnomeDesktop-WARNING: Could not create transient scope for PID 1713: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1713 does not exist.
Jun 30 05:39:14 ty-virtual-machine gnome-session-binary[1500]: GnomeDesktop-WARNING: Could not create transient scope for PID 1713: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1713 does not exist.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME FreeDesktop screensaver service.
Jun 30 05:39:14 ty-virtual-machine kernel: [   47.153086] rfkill: input handler disabled
Jun 30 05:39:14 ty-virtual-machine at-spi2-registr[1685]: Failed to register client: GDBus.Error:org.gnome.SessionManager.AlreadyRegistered: Unable to register client
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME FreeDesktop screensaver target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME RFKill support service.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME file sharing service.
Jun 30 05:39:14 ty-virtual-machine at-spi2-registr[1685]: Unable to register client with session manager
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME smartcard service.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME sound sample caching service.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:14 ty-virtual-machine gnome-session[1500]: gnome-session-binary[1500]: GnomeDesktop-WARNING: Could not create transient scope for PID 1793: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1793 does not exist.
Jun 30 05:39:14 ty-virtual-machine gnome-session-binary[1500]: GnomeDesktop-WARNING: Could not create transient scope for PID 1793: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1793 does not exist.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: message repeated 2 times: [ Started Application launched by gnome-session-binary.]
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME RFKill support target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME file sharing target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME smartcard target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME sound sample caching target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started GNOME printer notifications service.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Scheduled restart job, restart counter is at 1.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Reached target GNOME printer notifications target.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Stopped Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: snap.snapd-desktop-integration.snapd-desktop-integration.service: Consumed 2.700s CPU time.
Jun 30 05:39:14 ty-virtual-machine systemd[1350]: Started Service for snap application snapd-desktop-integration.snapd-desktop-integration.
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:39:15 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:39:15 ty-virtual-machine kernel: [   48.021887] audit: type=1400 audit(1782812355.412:52): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=1862 comm="snap-confine" capability=12  capname="net_admin"
Jun 30 05:39:15 ty-virtual-machine kernel: [   48.023134] audit: type=1400 audit(1782812355.416:53): apparmor="DENIED" operation="capable" class="cap" profile="/snap/snapd/20671/usr/lib/snapd/snap-confine" pid=1862 comm="snap-confine" capability=38  capname="perfmon"
Jun 30 05:39:15 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:39:15 ty-virtual-machine snapd-desktop-i[1956]: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Jun 30 05:39:15 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.freedesktop.portal.Desktop' unit='xdg-desktop-portal.service' requested by ':1.71' (uid=1000 pid=1956 comm="/snap/snapd-desktop-integration/83/usr/bin/snapd-d" label="snap.snapd-desktop-integration.snapd-desktop-integration (enforce)")
Jun 30 05:39:15 ty-virtual-machine systemd[1350]: Starting Portal service...
Jun 30 05:39:15 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.freedesktop.impl.portal.desktop.gnome' unit='xdg-desktop-portal-gnome.service' requested by ':1.72' (uid=1000 pid=1960 comm="/usr/libexec/xdg-desktop-portal " label="unconfined")
Jun 30 05:39:16 ty-virtual-machine systemd[1350]: Starting Portal service (GNOME implementation)...
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Started GNOME keyboard configuration service.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target GNOME keyboard configuration target.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Started GNOME power management service.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target GNOME power management target.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Started GNOME keyboard shortcuts service.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target GNOME keyboard shortcuts target.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Started GNOME Wacom tablet support service.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target GNOME Wacom tablet support target.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Started GNOME color management service.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target GNOME color management target.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target GNOME Session.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target GNOME Wayland Session (session: ubuntu).
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Reached target Current graphical user session.
Jun 30 05:39:17 ty-virtual-machine systemd[1350]: Condition check resulted in GNOME Initial Setup being skipped.
Jun 30 05:39:18 ty-virtual-machine snapd[752]: stateengine.go:149: state ensure error: persistent network error: Get "https://api.snapcraft.io/api/v1/snaps/sections": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 05:39:18 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.gnome.ScreenSaver' requested by ':1.63' (uid=1000 pid=1738 comm="/usr/libexec/gsd-power " label="unconfined")
Jun 30 05:39:18 ty-virtual-machine gsd-media-keys[1735]: Failed to grab accelerator for keybinding settings:playback-repeat
Jun 30 05:39:18 ty-virtual-machine gsd-media-keys[1735]: Failed to grab accelerator for keybinding settings:hibernate
Jun 30 05:39:18 ty-virtual-machine gnome-shell[1543]: GNOME Shell started at Tue Jun 30 2026 05:39:12 GMT-0400 (EDT)
Jun 30 05:39:18 ty-virtual-machine gnome-shell[1543]: Registering session with GDM
Jun 30 05:39:18 ty-virtual-machine gsd-sound[1181]: Error releasing name org.gnome.SettingsDaemon.Sound: The connection is closed
Jun 30 05:39:18 ty-virtual-machine gsd-screensaver[1179]: Error releasing name org.gnome.SettingsDaemon.ScreensaverProxy: The connection is closed
Jun 30 05:39:18 ty-virtual-machine gsd-print-notif[1155]: Error releasing name org.gnome.SettingsDaemon.PrintNotifications: The connection is closed
Jun 30 05:39:18 ty-virtual-machine ibus-daemon[1304]: GChildWatchSource: Exit status of a child process was requested but ECHILD was received by waitpid(). See the documentation of g_child_watch_source_new() for possible causes.
Jun 30 05:39:18 ty-virtual-machine gdm-launch-environment]: GLib-GObject: g_object_unref: assertion 'G_IS_OBJECT (object)' failed
Jun 30 05:39:18 ty-virtual-machine systemd[1]: session-c1.scope: Deactivated successfully.
Jun 30 05:39:18 ty-virtual-machine systemd[1]: session-c1.scope: Consumed 12.446s CPU time.
Jun 30 05:39:18 ty-virtual-machine systemd[867]: pulseaudio.service: Consumed 1.336s CPU time.
Jun 30 05:39:18 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.ScreenSaver'
Jun 30 05:39:18 ty-virtual-machine gsd-color[1711]: failed to get edid: unable to get EDID for output
Jun 30 05:39:19 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.impl.portal.desktop.gnome'
Jun 30 05:39:19 ty-virtual-machine systemd[1350]: Started Portal service (GNOME implementation).
Jun 30 05:39:19 ty-virtual-machine rtkit-daemon[887]: Supervising 9 threads of 5 processes of 2 users.
Jun 30 05:39:19 ty-virtual-machine rtkit-daemon[887]: message repeated 2 times: [ Supervising 9 threads of 5 processes of 2 users.]
Jun 30 05:39:19 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.freedesktop.impl.portal.desktop.gtk' unit='xdg-desktop-portal-gtk.service' requested by ':1.72' (uid=1000 pid=1960 comm="/usr/libexec/xdg-desktop-portal " label="unconfined")
Jun 30 05:39:19 ty-virtual-machine systemd[1350]: Starting Portal service (GTK/GNOME implementation)...
Jun 30 05:39:19 ty-virtual-machine systemd[1]: fprintd.service: Deactivated successfully.
Jun 30 05:39:19 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:39:19 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.impl.portal.desktop.gtk'
Jun 30 05:39:19 ty-virtual-machine systemd[1350]: Started Portal service (GTK/GNOME implementation).
Jun 30 05:39:19 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.portal.Desktop'
Jun 30 05:39:19 ty-virtual-machine systemd[1350]: Started Portal service.
Jun 30 05:39:19 ty-virtual-machine systemd[1350]: Startup finished in 11.804s.
Jun 30 05:39:19 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:39:19 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:39:20 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:39:20 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:39:20 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.FileManager1'
Jun 30 05:39:20 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.gnome.ArchiveManager1' requested by ':1.84' (uid=1000 pid=2032 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 30 05:39:20 ty-virtual-machine snapd-desktop-i[1956]: New theme: gtk=Yaru icon=Yaru cursor=Yaru, sound=Yaru
Jun 30 05:39:20 ty-virtual-machine snapd-desktop-i[1956]: All available theme snaps installed
Jun 30 05:39:20 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 30 05:39:20 ty-virtual-machine gnome-shell[1543]: DING: Detected async api for thumbnails
Jun 30 05:39:20 ty-virtual-machine gnome-shell[1543]: DING: GNOME nautilus 42.6
Jun 30 05:39:26 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.10' (uid=1000 pid=1439 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 05:39:26 ty-virtual-machine systemd[1350]: Starting Tracker metadata extractor...
Jun 30 05:39:26 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.Tracker3.Miner.Extract'
Jun 30 05:39:26 ty-virtual-machine systemd[1350]: Started Tracker metadata extractor.
Jun 30 05:39:28 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.gnome.Terminal' unit='gnome-terminal-server.service' requested by ':1.93' (uid=1000 pid=2111 comm="/usr/bin/gnome-terminal.real --wait " label="unconfined")
Jun 30 05:39:28 ty-virtual-machine systemd[1350]: Created slice Slice /app/org.gnome.Terminal.
Jun 30 05:39:28 ty-virtual-machine systemd[1350]: Starting GNOME Terminal Server...
Jun 30 05:39:28 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.Terminal'
Jun 30 05:39:28 ty-virtual-machine systemd[1350]: Started GNOME Terminal Server.
Jun 30 05:39:28 ty-virtual-machine systemd[1350]: Started VTE child process 2134 launched by gnome-terminal-server process 2116.
Jun 30 05:39:28 ty-virtual-machine systemd[1]: Stopping User Manager for UID 128...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped target Main User Target.
Jun 30 05:39:28 ty-virtual-machine gvfsd[903]: A connection to the bus can't be made
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping D-Bus User Message Bus...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping Virtual filesystem service - Apple File Conduit monitor...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping Virtual filesystem service...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping Virtual filesystem service - GNOME Online Accounts monitor...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping Virtual filesystem service - digital camera monitor...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping Virtual filesystem service - Media Transfer Protocol monitor...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping Virtual filesystem service - disk device monitor...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping PipeWire Media Session Manager...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping Tracker file system data miner...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping flatpak document portal service...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping sandboxed app permission store...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped Virtual filesystem service - Apple File Conduit monitor.
Jun 30 05:39:28 ty-virtual-machine systemd[1]: run-user-128-gvfs.mount: Deactivated successfully.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped PipeWire Media Session Manager.
Jun 30 05:39:28 ty-virtual-machine systemd[1]: run-user-128-doc.mount: Deactivated successfully.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped D-Bus User Message Bus.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped Virtual filesystem service - disk device monitor.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped Virtual filesystem service - Media Transfer Protocol monitor.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped Virtual filesystem service - digital camera monitor.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped flatpak document portal service.
Jun 30 05:39:28 ty-virtual-machine tracker-miner-fs-3[940]: OK
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped Virtual filesystem service - GNOME Online Accounts monitor.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped sandboxed app permission store.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped Virtual filesystem service.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopping PipeWire Multimedia Service...
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Stopped PipeWire Multimedia Service.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: Removed slice User Core Session Slice.
Jun 30 05:39:28 ty-virtual-machine systemd[867]: session.slice: Consumed 1.663s CPU time.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Stopped Tracker file system data miner.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: tracker-miner-fs-3.service: Consumed 1.367s CPU time.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Removed slice User Background Tasks Slice.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: background.slice: Consumed 2.020s CPU time.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Stopped target Basic System.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Stopped target Paths.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Stopped Pending report trigger for Ubuntu Report.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Stopped target Sockets.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Stopped target Timers.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed D-Bus User Message Bus Socket.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed GnuPG network certificate management daemon.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed GnuPG cryptographic agent and passphrase cache (restricted).
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed GnuPG cryptographic agent (ssh-agent emulation).
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed GnuPG cryptographic agent and passphrase cache.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed PipeWire Multimedia System Socket.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed debconf communication socket.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed Sound System.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed REST API socket for snapd user session agent.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Closed Speech Dispatcher Socket.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Removed slice User Application Slice.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: app.slice: Consumed 4.606s CPU time.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Reached target Shutdown.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Finished Exit the Session.
Jun 30 05:39:29 ty-virtual-machine systemd[867]: Reached target Exit the Session.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: user@128.service: Deactivated successfully.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: Stopped User Manager for UID 128.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: user@128.service: Consumed 8.893s CPU time.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: Stopping User Runtime Directory /run/user/128...
Jun 30 05:39:29 ty-virtual-machine systemd[1]: run-user-128.mount: Deactivated successfully.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: user-runtime-dir@128.service: Deactivated successfully.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: Stopped User Runtime Directory /run/user/128.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: Removed slice User Slice of UID 128.
Jun 30 05:39:29 ty-virtual-machine systemd[1]: user-128.slice: Consumed 21.362s CPU time.
Jun 30 05:39:30 ty-virtual-machine nautilus[1671]: Could not delete '.meta.isrunning': No such file or directory
Jun 30 05:39:33 ty-virtual-machine pulseaudio[1359]: GetManagedObjects() failed: org.freedesktop.DBus.Error.NoReply: Did not receive a reply. Possible causes include: the remote application did not send a reply, the message bus security policy blocked the reply, the reply timeout expired, or the network connection was broken.
Jun 30 05:39:38 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 60s"
Jun 30 05:39:47 ty-virtual-machine systemd[1]: systemd-localed.service: Deactivated successfully.
Jun 30 05:39:47 ty-virtual-machine systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 30 05:39:48 ty-virtual-machine geoclue[1122]: Service not used for 60 seconds. Shutting down..
Jun 30 05:39:48 ty-virtual-machine systemd[1]: geoclue.service: Deactivated successfully.
Jun 30 05:40:14 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:40:14 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:40:16 ty-virtual-machine ubuntu-appindicators@ubuntu.com[1543]: unable to update icon for software-update-available
Jun 30 05:40:16 ty-virtual-machine ubuntu-appindicators@ubuntu.com[1543]: unable to update icon for livepatch
Jun 30 05:40:18 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:40:18 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:40:18 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:40:18 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:40:18 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:40:38 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 120s"
Jun 30 05:40:49 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:40:49 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:40:49 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:40:49 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:40:49 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:40:55 ty-virtual-machine systemd[1350]: Started Application launched by gnome-shell.
Jun 30 05:40:56 ty-virtual-machine systemd[1350]: Started snap.firefox.firefox-a2568274-872d-4111-9424-0ded6a11f73d.scope.
Jun 30 05:40:56 ty-virtual-machine systemd[1]: tmp-snap.rootfs_k2w6oO.mount: Deactivated successfully.
Jun 30 05:40:56 ty-virtual-machine kernel: [  148.849217] audit: type=1400 audit(1782812456.240:54): apparmor="DENIED" operation="open" class="file" profile="snap-update-ns.firefox" name="/usr/local/share/" pid=2246 comm="5" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Jun 30 05:40:56 ty-virtual-machine firefox_firefox.desktop[2246]: update.go:85: cannot change mount namespace according to change mount (/var/lib/snapd/hostfs/usr/local/share/doc /usr/local/share/doc none bind,ro 0 0): cannot open directory "/usr/local/share": permission denied
Jun 30 05:40:56 ty-virtual-machine firefox_firefox.desktop[2246]: update.go:85: cannot change mount namespace according to change mount (/var/lib/snapd/hostfs/usr/share/gimp/2.0/help /usr/share/gimp/2.0/help none bind,ro 0 0): cannot open directory "/var/lib": permission denied
Jun 30 05:40:56 ty-virtual-machine firefox_firefox.desktop[2246]: update.go:85: cannot change mount namespace according to change mount (/var/lib/snapd/hostfs/usr/share/xubuntu-docs /usr/share/xubuntu-docs none bind,ro 0 0): cannot open directory "/var/lib": permission denied
Jun 30 05:40:56 ty-virtual-machine kernel: [  148.862691] audit: type=1400 audit(1782812456.256:55): apparmor="DENIED" operation="open" class="file" profile="snap-update-ns.firefox" name="/var/lib/" pid=2246 comm="5" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Jun 30 05:40:56 ty-virtual-machine kernel: [  148.865324] audit: type=1400 audit(1782812456.256:56): apparmor="DENIED" operation="open" class="file" profile="snap-update-ns.firefox" name="/var/lib/" pid=2246 comm="5" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Jun 30 05:40:57 ty-virtual-machine firefox[2220]: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Jun 30 05:40:58 ty-virtual-machine kernel: [  151.507791] audit: type=1107 audit(1782812458.900:57): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.12" pid=2220 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 30 05:40:58 ty-virtual-machine kernel: [  151.507791]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:40:58 ty-virtual-machine kernel: [  151.508670] audit: type=1107 audit(1782812458.900:58): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.110" pid=2220 label="snap.firefox.firefox" peer_pid=2218 peer_label="unconfined"
Jun 30 05:40:58 ty-virtual-machine kernel: [  151.508670]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:41:04 ty-virtual-machine rtkit-daemon[887]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:41:04 ty-virtual-machine rtkit-daemon[887]: message repeated 3 times: [ Supervising 6 threads of 3 processes of 1 users.]
Jun 30 05:41:04 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 2543 of process 2220 owned by '1000' RT at priority 10.
Jun 30 05:41:04 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:41:05 ty-virtual-machine rtkit-daemon[887]: message repeated 2 times: [ Supervising 7 threads of 4 processes of 1 users.]
Jun 30 05:41:05 ty-virtual-machine gnome-shell[1543]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 30 05:41:06 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='io.snapcraft.Settings' requested by ':1.106' (uid=1000 pid=2584 comm="dbus-send --print-reply=literal --session --dest=i" label="snap.firefox.firefox (enforce)")
Jun 30 05:41:06 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'io.snapcraft.Settings'
Jun 30 05:41:06 ty-virtual-machine io.snapcraft.Settings[2587]: userd.go:93: Starting snap userd
Jun 30 05:41:06 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:41:11 ty-virtual-machine rtkit-daemon[887]: message repeated 7 times: [ Supervising 7 threads of 4 processes of 1 users.]
Jun 30 05:41:14 ty-virtual-machine systemd[1350]: Started Application launched by gnome-session-binary.
Jun 30 05:41:16 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:41:16 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:41:19 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:41:19 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:41:19 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:41:19 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:41:19 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:41:19 ty-virtual-machine kernel: [  172.070762] audit: type=1107 audit(1782812479.460:59): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.122" pid=2220 label="snap.firefox.firefox" peer_pid=3105 peer_label="unconfined"
Jun 30 05:41:19 ty-virtual-machine kernel: [  172.070762]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:41:49 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:41:49 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:41:49 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:41:49 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:41:49 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:41:49 ty-virtual-machine kernel: [  202.320234] audit: type=1107 audit(1782812509.712:60): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.123" pid=2220 label="snap.firefox.firefox" peer_pid=3793 peer_label="unconfined"
Jun 30 05:41:49 ty-virtual-machine kernel: [  202.320234]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:41:57 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:41:57 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:42:19 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:42:19 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:42:19 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:42:19 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:42:19 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:42:19 ty-virtual-machine kernel: [  232.536385] audit: type=1107 audit(1782812539.928:61): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.125" pid=2220 label="snap.firefox.firefox" peer_pid=3825 peer_label="unconfined"
Jun 30 05:42:19 ty-virtual-machine kernel: [  232.536385]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:42:38 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 240s"
Jun 30 05:42:45 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:42:45 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:42:49 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:42:50 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:42:50 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:42:50 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:42:50 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:42:50 ty-virtual-machine kernel: [  262.783580] audit: type=1107 audit(1782812570.176:62): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.127" pid=2220 label="snap.firefox.firefox" peer_pid=3986 peer_label="unconfined"
Jun 30 05:42:50 ty-virtual-machine kernel: [  262.783580]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:43:03 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 05:43:12 ty-virtual-machine rtkit-daemon[887]: message repeated 3 times: [ Supervising 7 threads of 4 processes of 1 users.]
Jun 30 05:43:20 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:43:20 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:43:20 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:43:20 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:43:20 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:43:20 ty-virtual-machine kernel: [  293.000033] audit: type=1107 audit(1782812600.392:63): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.130" pid=2220 label="snap.firefox.firefox" peer_pid=4053 peer_label="unconfined"
Jun 30 05:43:20 ty-virtual-machine kernel: [  293.000033]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:43:41 ty-virtual-machine systemd[1]: Starting Download data for packages that failed at package install time...
Jun 30 05:43:42 ty-virtual-machine systemd[1]: update-notifier-download.service: Deactivated successfully.
Jun 30 05:43:42 ty-virtual-machine systemd[1]: Finished Download data for packages that failed at package install time.
Jun 30 05:43:50 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:43:50 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:43:50 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:43:50 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:43:50 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:43:50 ty-virtual-machine kernel: [  323.226413] audit: type=1107 audit(1782812630.616:64): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.131" pid=2220 label="snap.firefox.firefox" peer_pid=4064 peer_label="unconfined"
Jun 30 05:43:50 ty-virtual-machine kernel: [  323.226413]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:44:20 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:44:20 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:44:20 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:44:20 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:44:20 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:44:20 ty-virtual-machine kernel: [  353.461465] audit: type=1107 audit(1782812660.852:65): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.132" pid=2220 label="snap.firefox.firefox" peer_pid=4068 peer_label="unconfined"
Jun 30 05:44:20 ty-virtual-machine kernel: [  353.461465]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:44:50 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:44:50 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:44:50 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:44:51 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:44:51 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:44:51 ty-virtual-machine kernel: [  383.711601] audit: type=1107 audit(1782812691.104:66): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.133" pid=2220 label="snap.firefox.firefox" peer_pid=4071 peer_label="unconfined"
Jun 30 05:44:51 ty-virtual-machine kernel: [  383.711601]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:45:21 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:45:21 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:45:21 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:45:21 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:45:21 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:45:21 ty-virtual-machine kernel: [  413.932794] audit: type=1107 audit(1782812721.324:67): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.134" pid=2220 label="snap.firefox.firefox" peer_pid=4109 peer_label="unconfined"
Jun 30 05:45:21 ty-virtual-machine kernel: [  413.932794]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:45:51 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:45:51 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:45:51 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:45:51 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:45:51 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:45:51 ty-virtual-machine kernel: [  444.146949] audit: type=1107 audit(1782812751.536:68): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.135" pid=2220 label="snap.firefox.firefox" peer_pid=4114 peer_label="unconfined"
Jun 30 05:45:51 ty-virtual-machine kernel: [  444.146949]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:46:21 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:46:21 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:46:21 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:46:21 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:46:21 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:46:21 ty-virtual-machine kernel: [  474.360857] audit: type=1107 audit(1782812781.752:69): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.136" pid=2220 label="snap.firefox.firefox" peer_pid=4151 peer_label="unconfined"
Jun 30 05:46:21 ty-virtual-machine kernel: [  474.360857]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:46:38 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 480s"
Jun 30 05:46:51 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:46:51 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:46:51 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:46:51 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:46:51 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:46:51 ty-virtual-machine kernel: [  504.589357] audit: type=1107 audit(1782812811.980:70): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.137" pid=2220 label="snap.firefox.firefox" peer_pid=4155 peer_label="unconfined"
Jun 30 05:46:51 ty-virtual-machine kernel: [  504.589357]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:47:22 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:47:22 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:47:22 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:47:22 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:47:22 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:47:22 ty-virtual-machine kernel: [  534.816658] audit: type=1107 audit(1782812842.208:71): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.138" pid=2220 label="snap.firefox.firefox" peer_pid=4158 peer_label="unconfined"
Jun 30 05:47:22 ty-virtual-machine kernel: [  534.816658]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:47:33 ty-virtual-machine systemd[1350]: snap.firefox.firefox-a2568274-872d-4111-9424-0ded6a11f73d.scope: Consumed 1min 1.420s CPU time.
Jun 30 05:47:46 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.locale1' unit='dbus-org.freedesktop.locale1.service' requested by ':1.139' (uid=1000 pid=4190 comm="gnome-control-center display " label="unconfined")
Jun 30 05:47:46 ty-virtual-machine systemd[1]: Starting Locale Service...
Jun 30 05:47:46 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.locale1'
Jun 30 05:47:46 ty-virtual-machine systemd[1]: Started Locale Service.
Jun 30 05:47:52 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:47:52 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:47:52 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:47:52 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:47:52 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:47:54 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:47:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:48:06 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:48:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:48:09 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:48:10 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:48:17 ty-virtual-machine systemd[1]: systemd-localed.service: Deactivated successfully.
Jun 30 05:48:17 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:48:18 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:48:22 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:48:22 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.37' (uid=0 pid=752 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 30 05:48:22 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:48:22 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:48:22 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:48:40 ty-virtual-machine anacron[714]: Job `cron.weekly' started
Jun 30 05:48:40 ty-virtual-machine anacron[4262]: Updated timestamp for job `cron.weekly' to 2026-06-30
Jun 30 05:48:40 ty-virtual-machine anacron[714]: Job `cron.weekly' terminated
Jun 30 05:48:45 ty-virtual-machine snapd[752]: devicemgr.go:2399: no NTP sync after 10m0s, trying auto-refresh anyway
Jun 30 05:48:52 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 05:53:34 ty-virtual-machine systemd[1]: Starting Cleanup of Temporary Directories...
Jun 30 05:53:34 ty-virtual-machine systemd[1]: systemd-tmpfiles-clean.service: Deactivated successfully.
Jun 30 05:53:34 ty-virtual-machine systemd[1]: Finished Cleanup of Temporary Directories.
Jun 30 05:53:40 ty-virtual-machine anacron[714]: Job `cron.monthly' started
Jun 30 05:53:40 ty-virtual-machine anacron[4281]: Updated timestamp for job `cron.monthly' to 2026-06-30
Jun 30 05:53:40 ty-virtual-machine anacron[714]: Job `cron.monthly' terminated
Jun 30 05:53:40 ty-virtual-machine anacron[714]: Normal exit (2 jobs run)
Jun 30 05:53:40 ty-virtual-machine systemd[1]: anacron.service: Deactivated successfully.
Jun 30 05:54:38 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 960s"
Jun 30 05:58:00 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:00 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:58:08 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:08 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:58:12 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:12 ty-virtual-machine gnome-shell[1543]: Spurious clutter_actor_allocate called for actor 0x55cdee0fa440/<dashtodockContainer>[<Gjs_ubuntu-dock_ubuntu_com_docking_DashToDock>:0x55cdee0fa440] which isn't a descendent of the stage!
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:13 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:58:15 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:58:24 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:25 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:58:44 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:44 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:58:52 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:53 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:58:59 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:58:59 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:59:06 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:59:07 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:59:17 ty-virtual-machine gsd-color[1711]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 30 05:59:17 ty-virtual-machine gnome-shell[1543]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 30 05:59:33 ty-virtual-machine systemd[1350]: Started Application launched by gnome-shell.
Jun 30 05:59:33 ty-virtual-machine systemd[1350]: Started snap.snap-store.ubuntu-software-8cdd1d7a-4a5e-41cf-afce-74dd75cfb671.scope.
Jun 30 05:59:33 ty-virtual-machine systemd[1]: tmp-snap.rootfs_9r3pSI.mount: Deactivated successfully.
Jun 30 05:59:34 ty-virtual-machine snap-store_ubuntu-software.desktop[4534]: Warning: Schema “org.gnome.system.locale” has path “/system/locale/”.  Paths starting with “/apps/”, “/desktop/” or “/system/” are deprecated.
Jun 30 05:59:34 ty-virtual-machine snap-store_ubuntu-software.desktop[4534]: Warning: Schema “org.gnome.system.proxy” has path “/system/proxy/”.  Paths starting with “/apps/”, “/desktop/” or “/system/” are deprecated.
Jun 30 05:59:34 ty-virtual-machine snap-store_ubuntu-software.desktop[4534]: Warning: Schema “org.gnome.system.proxy.http” has path “/system/proxy/http/”.  Paths starting with “/apps/”, “/desktop/” or “/system/” are deprecated.
Jun 30 05:59:34 ty-virtual-machine snap-store_ubuntu-software.desktop[4534]: Warning: Schema “org.gnome.system.proxy.https” has path “/system/proxy/https/”.  Paths starting with “/apps/”, “/desktop/” or “/system/” are deprecated.
Jun 30 05:59:34 ty-virtual-machine snap-store_ubuntu-software.desktop[4534]: Warning: Schema “org.gnome.system.proxy.ftp” has path “/system/proxy/ftp/”.  Paths starting with “/apps/”, “/desktop/” or “/system/” are deprecated.
Jun 30 05:59:34 ty-virtual-machine snap-store_ubuntu-software.desktop[4534]: Warning: Schema “org.gnome.system.proxy.socks” has path “/system/proxy/socks/”.  Paths starting with “/apps/”, “/desktop/” or “/system/” are deprecated.
Jun 30 05:59:36 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.fwupd' unit='fwupd.service' requested by ':1.143' (uid=1000 pid=4361 comm="/snap/snap-store/959/usr/bin/snap-store " label="snap.snap-store.ubuntu-software (enforce)")
Jun 30 05:59:36 ty-virtual-machine systemd[1]: Starting Firmware update daemon...
Jun 30 05:59:37 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.fwupd'
Jun 30 05:59:37 ty-virtual-machine systemd[1]: Started Firmware update daemon.
Jun 30 05:59:37 ty-virtual-machine snap-store[4361]: plugin fwupd took 1.7 seconds to do setup
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.051419] audit: type=1107 audit(1782813578.444:72): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/PolicyKit1/Authority" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.3" pid=4361 label="snap.snap-store.ubuntu-software" peer_pid=741 peer_label="unconfined"
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.051419]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.053925] audit: type=1107 audit(1782813578.444:73): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/PolicyKit1/Authority" interface="org.freedesktop.PolicyKit1.Authority" member="CheckAuthorization" mask="send" name=":1.3" pid=4361 label="snap.snap-store.ubuntu-software" peer_pid=741 peer_label="unconfined"
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.053925]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.065898] audit: type=1107 audit(1782813578.456:74): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/PolicyKit1/Authority" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.3" pid=4361 label="snap.snap-store.ubuntu-software" peer_pid=741 peer_label="unconfined"
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.065898]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:59:38 ty-virtual-machine snap-store[4361]: enabled plugins: fwupd, os-release, packagekit-refine-repos, packagekit-refresh, appstream, hardcoded-blocklist, hardcoded-popular, modalias, packagekit, rewrite-resource, provenance, snap, systemd-updates, generic-updates, provenance-license, icons
Jun 30 05:59:38 ty-virtual-machine snap-store[4361]: disabled plugins: dpkg, dummy, fedora-langpacks, fedora-pkgdb-collections, repos
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.067060] audit: type=1107 audit(1782813578.460:75): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/PolicyKit1/Authority" interface="org.freedesktop.PolicyKit1.Authority" member="CheckAuthorization" mask="send" name=":1.3" pid=4361 label="snap.snap-store.ubuntu-software" peer_pid=741 peer_label="unconfined"
Jun 30 05:59:38 ty-virtual-machine kernel: [ 1271.067060]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:59:39 ty-virtual-machine kernel: [ 1272.197305] audit: type=1400 audit(1782813579.588:76): apparmor="DENIED" operation="open" class="file" profile="snap.snap-store.ubuntu-software" name="/etc/appstream.conf" pid=4361 comm="snap-store" requested_mask="r" denied_mask="r" fsuid=1000 ouid=0
Jun 30 05:59:39 ty-virtual-machine PackageKit: refresh-cache transaction /2_aacbaeae from uid 1000 finished with failed after 71ms
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.Builder.desktop/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.Calculator.desktop/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.clocks.desktop/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.Dictionary.desktop/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.Documents.desktop/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.Evince/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.gedit.desktop/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.Maps.desktop/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: adding wildcard app */*/*/org.gnome.Weather/* to plugin cache
Jun 30 05:59:39 ty-virtual-machine snap-store[4361]: Only 0 apps for recent list, hiding
Jun 30 05:59:39 ty-virtual-machine gnome-shell[1543]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 30 05:59:40 ty-virtual-machine snap-store[4361]: not handling error no-network for action refresh: Cannot refresh cache whilst offline
Jun 30 05:59:40 ty-virtual-machine snap-store[4361]: not handling error download-failed for action download: failed to download https://odrs.gnome.org/1.0/reviews/api/ratings: Cannot resolve hostname
Jun 30 05:59:40 ty-virtual-machine snap-store[4361]: not handling error not-supported for action refresh: failed to download file: Could not resolve host: cdn.fwupd.org
Jun 30 05:59:56 ty-virtual-machine systemd[1350]: Started Application launched by gnome-shell.
Jun 30 05:59:56 ty-virtual-machine systemd[1350]: Started snap.firefox.firefox-dada3597-7059-4fad-abae-01f352fcf38d.scope.
Jun 30 05:59:57 ty-virtual-machine firefox[4640]: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Jun 30 05:59:58 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.145' (uid=1000 pid=4640 comm="/snap/firefox/3836/usr/lib/firefox/firefox " label="snap.firefox.firefox (enforce)")
Jun 30 05:59:58 ty-virtual-machine kernel: [ 1291.456599] audit: type=1107 audit(1782813598.848:77): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.12" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 30 05:59:58 ty-virtual-machine kernel: [ 1291.456599]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:59:58 ty-virtual-machine systemd[1]: Starting Time & Date Service...
Jun 30 05:59:58 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 30 05:59:58 ty-virtual-machine systemd[1]: Started Time & Date Service.
Jun 30 05:59:59 ty-virtual-machine kernel: [ 1292.045569] audit: type=1107 audit(1782813599.436:78): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.146" pid=4640 label="snap.firefox.firefox" peer_pid=4804 peer_label="unconfined"
Jun 30 05:59:59 ty-virtual-machine kernel: [ 1292.045569]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:59:59 ty-virtual-machine kernel: [ 1292.055025] audit: type=1107 audit(1782813599.448:79): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/timedate1" interface="org.freedesktop.DBus.Properties" member="GetAll" mask="send" name=":1.146" pid=4640 label="snap.firefox.firefox" peer_pid=4804 peer_label="unconfined"
Jun 30 05:59:59 ty-virtual-machine kernel: [ 1292.055025]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 30 05:59:59 ty-virtual-machine rtkit-daemon[887]: Supervising 6 threads of 3 processes of 1 users.
Jun 30 05:59:59 ty-virtual-machine rtkit-daemon[887]: message repeated 3 times: [ Supervising 6 threads of 3 processes of 1 users.]
Jun 30 05:59:59 ty-virtual-machine rtkit-daemon[887]: Successfully made thread 4854 of process 4640 owned by '1000' RT at priority 10.
Jun 30 05:59:59 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 06:00:00 ty-virtual-machine gnome-shell[1543]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 30 06:00:00 ty-virtual-machine rtkit-daemon[887]: Supervising 7 threads of 4 processes of 1 users.
Jun 30 06:00:09 ty-virtual-machine rtkit-daemon[887]: message repeated 9 times: [ Supervising 7 threads of 4 processes of 1 users.]
Jun 30 06:00:12 ty-virtual-machine snap-store[4361]: not GsPlugin error snapd-error-quark:10: status-code=500 kind=(null) message=persistent network error: Get "https://api.snapcraft.io/api/v1/snaps/sections": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 06:00:12 ty-virtual-machine snap-store[4361]: failed to get categories: no categories to show
Jun 30 06:00:12 ty-virtual-machine snap-store[4361]: not handling error failed for action get-categories: status-code=500 kind=(null) message=persistent network error: Get "https://api.snapcraft.io/api/v1/snaps/sections": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 06:00:12 ty-virtual-machine snap-store[4361]: not handling error failed for action get-featured: persistent network error: Get "https://api.snapcraft.io/v2/snaps/find?architecture=amd64&category=featured&confinement=strict%2Cclassic&fields=base%2Cconfinement%2Clinks%2Ccontact%2Cdescription%2Cdownload%2Clicense%2Cprices%2Cprivate%2Cpublisher%2Crevision%2Csummary%2Ctitle%2Ctype%2Cversion%2Cwebsite%2Cstore-url%2Cmedia%2Ccommon-ids%2Ccategories%2Cchannel": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 06:00:12 ty-virtual-machine snap-store[4361]: not handling error failed for action get-popular: persistent network error: Get "https://api.snapcraft.io/v2/snaps/find?architecture=amd64&category=featured&confinement=strict%2Cclassic&fields=base%2Cconfinement%2Clinks%2Ccontact%2Cdescription%2Cdownload%2Clicense%2Cprices%2Cprivate%2Cpublisher%2Crevision%2Csummary%2Ctitle%2Ctype%2Cversion%2Cwebsite%2Cstore-url%2Cmedia%2Ccommon-ids%2Ccategories%2Cchannel": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 06:00:12 ty-virtual-machine PackageKit: resolve transaction /3_babdaead from uid 1000 finished with success after 76ms
Jun 30 06:00:12 ty-virtual-machine snap-store[4361]: Only 3 apps for popular list, hiding
Jun 30 06:00:12 ty-virtual-machine PackageKit: resolve transaction /4_cecacced from uid 1000 finished with success after 66ms
Jun 30 06:00:12 ty-virtual-machine PackageKit: resolve transaction /5_aeaecbdd from uid 1000 finished with success after 72ms
Jun 30 06:00:13 ty-virtual-machine PackageKit: search-file transaction /6_baedcdcd from uid 1000 finished with success after 1187ms
Jun 30 06:00:14 ty-virtual-machine PackageKit: search-file transaction /7_baacdecd from uid 1000 finished with success after 197ms
Jun 30 06:00:14 ty-virtual-machine PackageKit: get-details transaction /8_acbdaded from uid 1000 finished with success after 59ms
Jun 30 06:00:29 ty-virtual-machine systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 30 06:00:44 ty-virtual-machine snap-store[4361]: Failed to find refreshable snaps: status-code=500 kind=(null) message=cannot list updates: persistent network error: Post "https://api.snapcraft.io/v2/snaps/refresh": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 06:00:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: last_user_time (1349495) is greater than comparison timestamp (1349464).  This most likely represents a buggy client sending inaccurate timestamps in messages such as _NET_ACTIVE_WINDOW.  Trying to work around...
Jun 30 06:00:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: W3 appears to be one of the offending windows with a timestamp of 1349495.  Working around...
Jun 30 06:01:38 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.10' (uid=1000 pid=1439 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 30 06:01:38 ty-virtual-machine systemd[1350]: Starting Tracker metadata extractor...
Jun 30 06:01:38 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.freedesktop.Tracker3.Miner.Extract'
Jun 30 06:01:38 ty-virtual-machine systemd[1350]: Started Tracker metadata extractor.
Jun 30 06:01:41 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating service name='org.gnome.Nautilus' requested by ':1.84' (uid=1000 pid=2032 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 30 06:01:42 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.gnome.Nautilus'
Jun 30 06:01:42 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.155' (uid=1000 pid=5411 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 30 06:01:43 ty-virtual-machine systemd[1]: Starting Hostname Service...
Jun 30 06:01:43 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 30 06:01:43 ty-virtual-machine systemd[1]: Started Hostname Service.
Jun 30 06:01:56 ty-virtual-machine snap-store[4361]: not handling error failed for action search: persistent network error: Get "https://api.snapcraft.io/v2/snaps/find?architecture=amd64&confinement=strict%2Cclassic&fields=base%2Cconfinement%2Clinks%2Ccontact%2Cdescription%2Cdownload%2Clicense%2Cprices%2Cprivate%2Cpublisher%2Crevision%2Csummary%2Ctitle%2Ctype%2Cversion%2Cwebsite%2Cstore-url%2Cmedia%2Ccommon-ids%2Ccategories%2Cchannel&q=trae": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution
Jun 30 06:02:13 ty-virtual-machine systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 30 06:10:39 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 1800s"
Jun 30 06:14:14 ty-virtual-machine kernel: [ 2146.757982] workqueue: e1000_watchdog [e1000] hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
Jun 30 06:14:14 ty-virtual-machine kernel: [ 2146.803611] workqueue: psi_avgs_work hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
Jun 30 06:14:14 ty-virtual-machine kernel: [ 2147.011713] workqueue: psi_avgs_work hogged CPU for >10000us 8 times, consider switching to WQ_UNBOUND
Jun 30 06:16:55 ty-virtual-machine systemd[1350]: Started VTE child process 5518 launched by gnome-terminal-server process 2116.
Jun 30 06:17:01 ty-virtual-machine CRON[5526]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 30 06:17:21 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 30 06:17:21 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 30 06:17:22 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 30 06:17:22 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 30 06:17:22 ty-virtual-machine python3[5551]: Unable to parse build date from uname version
Jun 30 06:17:22 ty-virtual-machine python3[5551]: Falling back to using timestamp of kernel changelog
Jun 30 06:17:22 ty-virtual-machine python3[5551]: Error updating the cache: [Errno -3] Temporary failure in name resolution
Jun 30 06:17:22 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 30 06:17:22 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 30 06:18:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: last_user_time (2429265) is greater than comparison timestamp (2429234).  This most likely represents a buggy client sending inaccurate timestamps in messages such as _NET_ACTIVE_WINDOW.  Trying to work around...
Jun 30 06:18:56 ty-virtual-machine gnome-shell[1543]: Window manager warning: W3 appears to be one of the offending windows with a timestamp of 2429265.  Working around...
Jun 30 06:18:57 ty-virtual-machine gnome-shell[1543]: Window manager warning: last_user_time (2429654) is greater than comparison timestamp (2429622).  This most likely represents a buggy client sending inaccurate timestamps in messages such as _NET_ACTIVE_WINDOW.  Trying to work around...
Jun 30 06:18:57 ty-virtual-machine gnome-shell[1543]: Window manager warning: W3 appears to be one of the offending windows with a timestamp of 2429654.  Working around...
Jun 30 06:19:09 ty-virtual-machine gnome-shell[1543]: Window manager warning: last_user_time (2441616) is greater than comparison timestamp (2441429).  This most likely represents a buggy client sending inaccurate timestamps in messages such as _NET_ACTIVE_WINDOW.  Trying to work around...
Jun 30 06:19:09 ty-virtual-machine gnome-shell[1543]: Window manager warning: W3 appears to be one of the offending windows with a timestamp of 2441616.  Working around...
Jun 30 06:20:47 ty-virtual-machine gnome-shell[1543]: Window manager warning: last_user_time (2540453) is greater than comparison timestamp (2540422).  This most likely represents a buggy client sending inaccurate timestamps in messages such as _NET_ACTIVE_WINDOW.  Trying to work around...
Jun 30 06:20:47 ty-virtual-machine gnome-shell[1543]: Window manager warning: W3 appears to be one of the offending windows with a timestamp of 2540453.  Working around...
Jun 30 06:20:48 ty-virtual-machine gnome-shell[1543]: Window manager warning: last_user_time (2540876) is greater than comparison timestamp (2540827).  This most likely represents a buggy client sending inaccurate timestamps in messages such as _NET_ACTIVE_WINDOW.  Trying to work around...
Jun 30 06:20:48 ty-virtual-machine gnome-shell[1543]: Window manager warning: W3 appears to be one of the offending windows with a timestamp of 2540876.  Working around...
Jun 30 06:25:01 ty-virtual-machine CRON[5657]: (root) CMD (test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily ))
Jun 30 06:26:49 ty-virtual-machine systemd[1]: Starting Daily apt upgrade and clean activities...
Jun 30 06:27:19 ty-virtual-machine apt-helper[5697]: E: Sub-process nm-online returned an error code (1)
Jun 30 06:27:20 ty-virtual-machine systemd[1]: apt-daily-upgrade.service: Deactivated successfully.
Jun 30 06:27:20 ty-virtual-machine systemd[1]: Finished Daily apt upgrade and clean activities.
Jun 30 06:27:20 ty-virtual-machine systemd[1]: apt-daily-upgrade.service: Consumed 1.145s CPU time.
Jun 30 06:28:02 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 30 06:28:02 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 30 06:28:02 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 30 06:28:02 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 30 06:28:02 ty-virtual-machine python3[5850]: Unable to parse build date from uname version
Jun 30 06:28:02 ty-virtual-machine python3[5850]: Falling back to using timestamp of kernel changelog
Jun 30 06:28:02 ty-virtual-machine python3[5850]: Error updating the cache: [Errno -3] Temporary failure in name resolution
Jun 30 06:28:02 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 30 06:28:02 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 30 06:35:23 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 30 06:35:23 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 30 06:35:23 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 30 06:35:23 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 30 06:35:23 ty-virtual-machine python3[5932]: Unable to parse build date from uname version
Jun 30 06:35:23 ty-virtual-machine python3[5932]: Falling back to using timestamp of kernel changelog
Jun 30 06:35:24 ty-virtual-machine python3[5932]: Error updating the cache: [Errno -3] Temporary failure in name resolution
Jun 30 06:35:24 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 30 06:35:24 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 30 06:35:42 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 30 06:35:42 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 30 06:35:42 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 30 06:35:42 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 30 06:35:42 ty-virtual-machine python3[5959]: Unable to parse build date from uname version
Jun 30 06:35:42 ty-virtual-machine python3[5959]: Falling back to using timestamp of kernel changelog
Jun 30 06:35:42 ty-virtual-machine python3[5959]: Error updating the cache: [Errno -3] Temporary failure in name resolution
Jun 30 06:35:42 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 30 06:35:42 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 30 06:37:25 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 30 06:37:25 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 30 06:37:25 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 30 06:37:25 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 30 06:37:25 ty-virtual-machine python3[6008]: Unable to parse build date from uname version
Jun 30 06:37:25 ty-virtual-machine python3[6008]: Falling back to using timestamp of kernel changelog
Jun 30 06:37:25 ty-virtual-machine python3[6008]: Error updating the cache: [Errno -3] Temporary failure in name resolution
Jun 30 06:37:25 ty-virtual-machine kernel: [ 3538.244140] e1000: ens33 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: None
Jun 30 06:37:25 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 30 06:37:25 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6488] device (ens33): carrier: link connected
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6501] device (ens33): state change: unavailable -> disconnected (reason 'carrier-changed', sys-iface-state: 'managed')
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6587] policy: auto-activating connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6597] device (ens33): Activation: starting connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6599] device (ens33): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6602] manager: NetworkManager state is now CONNECTING
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6621] device (ens33): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6666] device (ens33): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:37:25 ty-virtual-machine NetworkManager[721]: <info>  [1782815845.6746] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 30 06:37:25 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:37:25 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv6 for mDNS.
Jun 30 06:37:25 ty-virtual-machine avahi-daemon[716]: Registering new address record for fe80::be9b:7858:e304:8e96 on ens33.*.
Jun 30 06:37:27 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 06:37:27 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 06:37:27 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 06:37:27 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 06:37:37 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4235] device (ens33): state change: ip-config -> failed (reason 'ip-config-unavailable', sys-iface-state: 'managed')
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4311] manager: NetworkManager state is now DISCONNECTED
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <warn>  [1782815891.4368] device (ens33): Activation: failed for connection 'Wired connection 1'
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4374] device (ens33): state change: failed -> disconnected (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:11 ty-virtual-machine avahi-daemon[716]: Withdrawing address record for fe80::be9b:7858:e304:8e96 on ens33.
Jun 30 06:38:11 ty-virtual-machine avahi-daemon[716]: Leaving mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:38:11 ty-virtual-machine avahi-daemon[716]: Interface ens33.IPv6 no longer relevant for mDNS.
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4810] dhcp4 (ens33): canceled DHCP transaction
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4843] policy: auto-activating connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4864] device (ens33): Activation: starting connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4869] device (ens33): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:11 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4900] manager: NetworkManager state is now CONNECTING
Jun 30 06:38:11 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4903] device (ens33): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:11 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv6 for mDNS.
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.4944] device (ens33): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:11 ty-virtual-machine NetworkManager[721]: <info>  [1782815891.5028] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 30 06:38:11 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 06:38:11 ty-virtual-machine avahi-daemon[716]: Registering new address record for fe80::be9b:7858:e304:8e96 on ens33.*.
Jun 30 06:38:11 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 06:38:11 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 06:38:18 ty-virtual-machine gnome-shell[1543]: libinput error: event2  - VirtualPS/2 VMware VMMouse: client bug: event processing lagging behind by 37ms, your system is too slow
Jun 30 06:38:23 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 06:38:37 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.139' (uid=1000 pid=4190 comm="gnome-control-center display " label="unconfined")
Jun 30 06:38:37 ty-virtual-machine systemd[1]: Starting Hostname Service...
Jun 30 06:38:37 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 30 06:38:37 ty-virtual-machine systemd[1]: Started Hostname Service.
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4225] device (ens33): state change: ip-config -> failed (reason 'ip-config-unavailable', sys-iface-state: 'managed')
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4229] manager: NetworkManager state is now DISCONNECTED
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <warn>  [1782815936.4233] device (ens33): Activation: failed for connection 'Wired connection 1'
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4235] device (ens33): state change: failed -> disconnected (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:56 ty-virtual-machine avahi-daemon[716]: Withdrawing address record for fe80::be9b:7858:e304:8e96 on ens33.
Jun 30 06:38:56 ty-virtual-machine avahi-daemon[716]: Leaving mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:38:56 ty-virtual-machine avahi-daemon[716]: Interface ens33.IPv6 no longer relevant for mDNS.
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4486] dhcp4 (ens33): canceled DHCP transaction
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4492] policy: auto-activating connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4499] device (ens33): Activation: starting connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4499] device (ens33): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4500] manager: NetworkManager state is now CONNECTING
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4501] device (ens33): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:56 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4521] device (ens33): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:38:56 ty-virtual-machine NetworkManager[721]: <info>  [1782815936.4615] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 30 06:38:56 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:38:56 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv6 for mDNS.
Jun 30 06:38:56 ty-virtual-machine avahi-daemon[716]: Registering new address record for fe80::be9b:7858:e304:8e96 on ens33.*.
Jun 30 06:38:56 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 06:38:56 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 06:38:56 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 06:39:07 ty-virtual-machine systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 30 06:39:07 ty-virtual-machine NetworkManager[721]: <info>  [1782815947.8657] device (ens33): state change: ip-config -> deactivating (reason 'user-requested', sys-iface-state: 'managed')
Jun 30 06:39:07 ty-virtual-machine NetworkManager[721]: <info>  [1782815947.8661] manager: NetworkManager state is now DISCONNECTING
Jun 30 06:39:07 ty-virtual-machine NetworkManager[721]: <info>  [1782815947.8671] audit: op="device-disconnect" interface="ens33" ifindex=2 pid=4190 uid=1000 result="success"
Jun 30 06:39:07 ty-virtual-machine NetworkManager[721]: <info>  [1782815947.8922] device (ens33): state change: deactivating -> disconnected (reason 'user-requested', sys-iface-state: 'managed')
Jun 30 06:39:07 ty-virtual-machine avahi-daemon[716]: Withdrawing address record for fe80::be9b:7858:e304:8e96 on ens33.
Jun 30 06:39:07 ty-virtual-machine avahi-daemon[716]: Leaving mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:39:07 ty-virtual-machine avahi-daemon[716]: Interface ens33.IPv6 no longer relevant for mDNS.
Jun 30 06:39:07 ty-virtual-machine NetworkManager[721]: <info>  [1782815947.9339] dhcp4 (ens33): canceled DHCP transaction
Jun 30 06:39:07 ty-virtual-machine NetworkManager[721]: <info>  [1782815947.9363] manager: NetworkManager state is now DISCONNECTED
Jun 30 06:39:09 ty-virtual-machine NetworkManager[721]: <info>  [1782815949.0278] device (ens33): Activation: starting connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:39:09 ty-virtual-machine NetworkManager[721]: <info>  [1782815949.0280] audit: op="connection-activate" uuid="578a3f49-da2b-3bab-9836-6628f03ec174" name="Wired connection 1" pid=4190 uid=1000 result="success"
Jun 30 06:39:09 ty-virtual-machine NetworkManager[721]: <info>  [1782815949.0282] device (ens33): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Jun 30 06:39:09 ty-virtual-machine NetworkManager[721]: <info>  [1782815949.0284] manager: NetworkManager state is now CONNECTING
Jun 30 06:39:09 ty-virtual-machine NetworkManager[721]: <info>  [1782815949.0286] device (ens33): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:39:09 ty-virtual-machine NetworkManager[721]: <info>  [1782815949.0326] device (ens33): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:39:09 ty-virtual-machine NetworkManager[721]: <info>  [1782815949.0436] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 30 06:39:09 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:39:09 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv6 for mDNS.
Jun 30 06:39:09 ty-virtual-machine avahi-daemon[716]: Registering new address record for fe80::be9b:7858:e304:8e96 on ens33.*.
Jun 30 06:39:19 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 06:39:20 ty-virtual-machine kernel: [ 3653.187139] e1000: ens33 NIC Link is Down
Jun 30 06:39:21 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 06:39:21 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 06:39:21 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 06:39:21 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 06:39:22 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Activating via systemd: service name='org.bluez.obex' unit='dbus-org.bluez.obex.service' requested by ':1.117' (uid=1000 pid=4190 comm="gnome-control-center display " label="unconfined")
Jun 30 06:39:22 ty-virtual-machine systemd[1350]: Starting Bluetooth OBEX service...
Jun 30 06:39:22 ty-virtual-machine obexd[6185]: OBEX daemon 5.64
Jun 30 06:39:22 ty-virtual-machine dbus-daemon[1382]: [session uid=1000 pid=1382] Successfully activated service 'org.bluez.obex'
Jun 30 06:39:22 ty-virtual-machine systemd[1350]: Started Bluetooth OBEX service.
Jun 30 06:39:26 ty-virtual-machine NetworkManager[721]: <info>  [1782815966.5851] device (ens33): state change: ip-config -> unavailable (reason 'carrier-changed', sys-iface-state: 'managed')
Jun 30 06:39:26 ty-virtual-machine NetworkManager[721]: <info>  [1782815966.6007] dhcp4 (ens33): canceled DHCP transaction
Jun 30 06:39:26 ty-virtual-machine avahi-daemon[716]: Withdrawing address record for fe80::be9b:7858:e304:8e96 on ens33.
Jun 30 06:39:26 ty-virtual-machine avahi-daemon[716]: Leaving mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:39:26 ty-virtual-machine avahi-daemon[716]: Interface ens33.IPv6 no longer relevant for mDNS.
Jun 30 06:39:26 ty-virtual-machine NetworkManager[721]: <info>  [1782815966.6132] manager: NetworkManager state is now DISCONNECTED
Jun 30 06:39:32 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 06:40:00 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.139' (uid=1000 pid=4190 comm="gnome-control-center display " label="unconfined")
Jun 30 06:40:00 ty-virtual-machine systemd[1]: Starting Hostname Service...
Jun 30 06:40:00 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 30 06:40:00 ty-virtual-machine systemd[1]: Started Hostname Service.
Jun 30 06:40:30 ty-virtual-machine systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 30 06:40:39 ty-virtual-machine ubuntu-report[1374]: level=error msg="data were not delivered successfully to metrics server, retrying in 1800s"
Jun 30 06:40:50 ty-virtual-machine dhclient[6217]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 3 (xid=0xd0442c1a)
Jun 30 06:40:52 ty-virtual-machine NetworkManager[721]: <info>  [1782816052.4140] failed to open /run/network/ifstate
Jun 30 06:40:54 ty-virtual-machine dhclient[6217]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 5 (xid=0xd0442c1a)
Jun 30 06:40:59 ty-virtual-machine dhclient[6217]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 7 (xid=0xd0442c1a)
Jun 30 06:41:06 ty-virtual-machine dhclient[6217]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 12 (xid=0xd0442c1a)
Jun 30 06:41:18 ty-virtual-machine dhclient[6217]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 15 (xid=0xd0442c1a)
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6475] device (ens33): carrier: link connected
Jun 30 06:43:40 ty-virtual-machine kernel: [ 3913.251384] e1000: ens33 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: None
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6476] device (ens33): state change: unavailable -> disconnected (reason 'carrier-changed', sys-iface-state: 'managed')
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6560] policy: auto-activating connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6567] device (ens33): Activation: starting connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6568] device (ens33): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6571] manager: NetworkManager state is now CONNECTING
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6573] device (ens33): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6652] device (ens33): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:43:40 ty-virtual-machine NetworkManager[721]: <info>  [1782816220.6737] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 30 06:43:40 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:43:40 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv6 for mDNS.
Jun 30 06:43:40 ty-virtual-machine avahi-daemon[716]: Registering new address record for fe80::be9b:7858:e304:8e96 on ens33.*.
Jun 30 06:43:42 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 06:43:42 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 06:43:42 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 06:43:42 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 06:43:52 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4227] device (ens33): state change: ip-config -> failed (reason 'ip-config-unavailable', sys-iface-state: 'managed')
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4237] manager: NetworkManager state is now DISCONNECTED
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <warn>  [1782816266.4241] device (ens33): Activation: failed for connection 'Wired connection 1'
Jun 30 06:44:26 ty-virtual-machine avahi-daemon[716]: Withdrawing address record for fe80::be9b:7858:e304:8e96 on ens33.
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4244] device (ens33): state change: failed -> disconnected (reason 'none', sys-iface-state: 'managed')
Jun 30 06:44:26 ty-virtual-machine avahi-daemon[716]: Leaving mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:44:26 ty-virtual-machine avahi-daemon[716]: Interface ens33.IPv6 no longer relevant for mDNS.
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4818] dhcp4 (ens33): canceled DHCP transaction
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4850] policy: auto-activating connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4862] device (ens33): Activation: starting connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4868] device (ens33): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4875] manager: NetworkManager state is now CONNECTING
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4881] device (ens33): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:44:26 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4924] device (ens33): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:44:26 ty-virtual-machine NetworkManager[721]: <info>  [1782816266.4993] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 30 06:44:26 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:44:26 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv6 for mDNS.
Jun 30 06:44:26 ty-virtual-machine avahi-daemon[716]: Registering new address record for fe80::be9b:7858:e304:8e96 on ens33.*.
Jun 30 06:44:26 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 06:44:26 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 06:44:26 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 06:44:38 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 30 06:44:59 ty-virtual-machine kernel: [ 3991.874835] e1000: ens33 NIC Link is Down
Jun 30 06:44:59 ty-virtual-machine kernel: [ 3991.875252] e1000 0000:02:01.0 ens33: Reset adapter
Jun 30 06:45:05 ty-virtual-machine NetworkManager[721]: <info>  [1782816305.2781] device (ens33): state change: ip-config -> unavailable (reason 'carrier-changed', sys-iface-state: 'managed')
Jun 30 06:45:05 ty-virtual-machine NetworkManager[721]: <info>  [1782816305.2933] dhcp4 (ens33): canceled DHCP transaction
Jun 30 06:45:05 ty-virtual-machine avahi-daemon[716]: Withdrawing address record for fe80::be9b:7858:e304:8e96 on ens33.
Jun 30 06:45:05 ty-virtual-machine avahi-daemon[716]: Leaving mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:45:05 ty-virtual-machine avahi-daemon[716]: Interface ens33.IPv6 no longer relevant for mDNS.
Jun 30 06:45:05 ty-virtual-machine NetworkManager[721]: <info>  [1782816305.3061] manager: NetworkManager state is now DISCONNECTED
Jun 30 06:45:07 ty-virtual-machine kernel: [ 4000.036707] e1000: ens33 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: None
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4331] device (ens33): carrier: link connected
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4336] device (ens33): state change: unavailable -> disconnected (reason 'carrier-changed', sys-iface-state: 'managed')
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4418] policy: auto-activating connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4434] device (ens33): Activation: starting connection 'Wired connection 1' (578a3f49-da2b-3bab-9836-6628f03ec174)
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4438] device (ens33): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4445] manager: NetworkManager state is now CONNECTING
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4451] device (ens33): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:45:07 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4496] device (ens33): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Jun 30 06:45:07 ty-virtual-machine NetworkManager[721]: <info>  [1782816307.4589] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 30 06:45:07 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::be9b:7858:e304:8e96.
Jun 30 06:45:07 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv6 for mDNS.
Jun 30 06:45:07 ty-virtual-machine avahi-daemon[716]: Registering new address record for fe80::be9b:7858:e304:8e96 on ens33.*.
Jun 30 06:45:07 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 30 06:45:07 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 30 06:45:07 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.4712] dhcp4 (ens33): state changed new lease, address=192.168.203.161
Jun 30 06:45:08 ty-virtual-machine avahi-daemon[716]: Joining mDNS multicast group on interface ens33.IPv4 with address 192.168.203.161.
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.4786] device (ens33): state change: ip-config -> ip-check (reason 'none', sys-iface-state: 'managed')
Jun 30 06:45:08 ty-virtual-machine avahi-daemon[716]: New relevant interface ens33.IPv4 for mDNS.
Jun 30 06:45:08 ty-virtual-machine avahi-daemon[716]: Registering new address record for 192.168.203.161 on ens33.IPv4.
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.4961] device (ens33): state change: ip-check -> secondaries (reason 'none', sys-iface-state: 'managed')
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.4977] device (ens33): state change: secondaries -> activated (reason 'none', sys-iface-state: 'managed')
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.4981] manager: NetworkManager state is now CONNECTED_LOCAL
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.4984] manager: NetworkManager state is now CONNECTED_SITE
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.5017] policy: set 'Wired connection 1' (ens33) as default for IPv4 routing and DNS
Jun 30 06:45:08 ty-virtual-machine NetworkManager[721]: <info>  [1782816308.5043] device (ens33): Activation: successful, device activated.
Jun 30 06:45:08 ty-virtual-machine systemd-resolved[518]: Failed to save link data /run/systemd/resolve/netif/2: Permission denied
Jun 30 06:45:08 ty-virtual-machine systemd-resolved[518]: ens33: Bus client set search domain list to: localdomain
Jun 30 06:45:08 ty-virtual-machine systemd-resolved[518]: Failed to save link data /run/systemd/resolve/netif/2: Permission denied
Jun 30 06:45:08 ty-virtual-machine systemd-resolved[518]: ens33: Bus client set default route setting: yes
Jun 30 06:45:08 ty-virtual-machine systemd-resolved[518]: Failed to save link data /run/systemd/resolve/netif/2: Permission denied
Jun 30 06:45:08 ty-virtual-machine systemd-resolved[518]: ens33: Bus client set DNS server list to: 192.168.203.2
Jun 30 06:45:08 ty-virtual-machine systemd-resolved[518]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.203.2.
Jun 30 06:45:09 ty-virtual-machine NetworkManager[721]: <info>  [1782816309.1767] manager: NetworkManager state is now CONNECTED_GLOBAL
Jun 30 06:45:11 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 30 06:45:11 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 30 06:45:12 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 30 06:45:12 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 30 06:45:12 ty-virtual-machine python3[6373]: Unable to parse build date from uname version
Jun 30 06:45:12 ty-virtual-machine python3[6373]: Falling back to using timestamp of kernel changelog
Jun 29 22:45:12 ty-virtual-machine systemd-resolved[518]: Clock change detected. Flushing caches.
Jun 29 22:45:12 ty-virtual-machine systemd-timesyncd[519]: Initial synchronization to time server 185.125.190.57:123 (ntp.ubuntu.com).
Jun 29 22:45:12 ty-virtual-machine systemd[1]: Starting Message of the Day...
Jun 29 22:45:12 ty-virtual-machine systemd[1]: motd-news.service: Deactivated successfully.
Jun 29 22:45:12 ty-virtual-machine systemd[1]: Finished Message of the Day.
Jun 29 22:45:18 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 29 22:45:19 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 29 22:45:19 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 29 22:45:19 ty-virtual-machine systemd[1]: esm-cache.service: Consumed 1.856s CPU time.
Jun 29 22:45:29 ty-virtual-machine snap-store[4361]: not handling error not-supported for action refresh: failed to download file: Failed to connect to cdn.fwupd.org port 443 after 21078 ms: Connection refused
Jun 29 22:45:29 ty-virtual-machine packagekitd[1123]: Could not get lock /var/lib/apt/lists/lock. It is held by process 6364 (apt-get)
Jun 29 22:45:29 ty-virtual-machine packagekitd[1123]: Be aware that removing the lock file is not a solution and may break your system.
Jun 29 22:45:29 ty-virtual-machine packagekitd[1123]: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:45:29 ty-virtual-machine PackageKit: refresh-cache transaction /9_cbdcbbdb from uid 1000 finished with failed after 78ms
Jun 29 22:45:29 ty-virtual-machine snap-store[4361]: not handling error download-failed for action refresh: E: Could not get lock /var/lib/apt/lists/lock. It is held by process 6364 (apt-get)#012W: Be aware that removing the lock file is not a solution and may break your system.#012E: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:45:29 ty-virtual-machine snap-store[4361]: not handling error download-failed for action download: failed to download https://odrs.gnome.org/1.0/reviews/api/ratings: SSL handshake failed
Jun 29 22:45:31 ty-virtual-machine snapd[752]: storehelpers.go:791: cannot refresh: snap has no updates available: "bare", "gtk-common-themes"
Jun 29 22:45:31 ty-virtual-machine PackageKit: get-updates transaction /10_ebedbcae from uid 1000 finished with success after 250ms
Jun 29 22:45:33 ty-virtual-machine snap-store[4361]: not handling error not-supported for action refresh: failed to download file: Failed to connect to cdn.fwupd.org port 443 after 21055 ms: Connection refused
Jun 29 22:45:33 ty-virtual-machine packagekitd[1123]: Could not get lock /var/lib/apt/lists/lock. It is held by process 6364 (apt-get)
Jun 29 22:45:33 ty-virtual-machine packagekitd[1123]: Be aware that removing the lock file is not a solution and may break your system.
Jun 29 22:45:33 ty-virtual-machine packagekitd[1123]: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:45:33 ty-virtual-machine PackageKit: refresh-cache transaction /11_cdbbbece from uid 1000 finished with failed after 281ms
Jun 29 22:45:33 ty-virtual-machine snap-store[4361]: not handling error download-failed for action refresh: E: Could not get lock /var/lib/apt/lists/lock. It is held by process 6364 (apt-get)#012W: Be aware that removing the lock file is not a solution and may break your system.#012E: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:45:34 ty-virtual-machine snap-store[4361]: not handling error download-failed for action download: failed to download https://odrs.gnome.org/1.0/reviews/api/ratings: SSL handshake failed
Jun 29 22:45:35 ty-virtual-machine snapd[752]: storehelpers.go:791: cannot refresh: snap has no updates available: "bare", "gtk-common-themes"
Jun 29 22:45:35 ty-virtual-machine PackageKit: get-updates transaction /12_bcbaecbe from uid 1000 finished with success after 237ms
Jun 29 22:45:49 ty-virtual-machine packagekitd[1123]: Could not get lock /var/lib/apt/lists/lock. It is held by process 6364 (apt-get)
Jun 29 22:45:49 ty-virtual-machine packagekitd[1123]: Be aware that removing the lock file is not a solution and may break your system.
Jun 29 22:45:49 ty-virtual-machine packagekitd[1123]: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:45:49 ty-virtual-machine PackageKit: refresh-cache transaction /13_bdbdeece from uid 1000 finished with failed after 7092ms
Jun 29 22:45:49 ty-virtual-machine snap-store[4361]: not handling error download-failed for action refresh: E: Could not get lock /var/lib/apt/lists/lock. It is held by process 6364 (apt-get)#012W: Be aware that removing the lock file is not a solution and may break your system.#012E: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:45:53 ty-virtual-machine kernel: [ 4046.222464] audit: type=1326 audit(1782787553.054:80): auid=1000 uid=1000 gid=1000 ses=3 subj=snap.snap-store.ubuntu-software pid=4361 comm="pool-org.gnome." exe="/snap/snap-store/959/usr/bin/snap-store" sig=0 arch=c000003e syscall=93 compat=0 ip=0x7fb666ee9a9b code=0x50000
Jun 29 22:45:53 ty-virtual-machine snap-store[4361]: not handling error download-failed for action download: failed to download https://odrs.gnome.org/1.0/reviews/api/ratings: SSL handshake failed
Jun 29 22:45:54 ty-virtual-machine snapd[752]: storehelpers.go:791: cannot refresh: snap has no updates available: "bare", "gtk-common-themes"
Jun 29 22:45:58 ty-virtual-machine kernel: [ 4051.849334] workqueue: blk_mq_run_work_fn hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
Jun 29 22:46:00 ty-virtual-machine PackageKit: get-updates transaction /14_aebbacbc from uid 1000 finished with success after 5774ms
Jun 29 22:46:14 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 29 22:46:14 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 29 22:46:14 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 29 22:46:14 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 29 22:46:16 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 29 22:46:16 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 29 22:46:23 ty-virtual-machine packagekitd[1123]: Could not get lock /var/lib/apt/lists/lock. It is held by process 7028 (apt)
Jun 29 22:46:23 ty-virtual-machine packagekitd[1123]: Be aware that removing the lock file is not a solution and may break your system.
Jun 29 22:46:23 ty-virtual-machine packagekitd[1123]: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:46:23 ty-virtual-machine PackageKit: refresh-cache transaction /15_eabcbddb from uid 1000 finished with failed after 5056ms
Jun 29 22:46:23 ty-virtual-machine snap-store[4361]: not handling error download-failed for action refresh: E: Could not get lock /var/lib/apt/lists/lock. It is held by process 7028 (apt)#012W: Be aware that removing the lock file is not a solution and may break your system.#012E: Unable to lock directory /var/lib/apt/lists/
Jun 29 22:46:24 ty-virtual-machine snap-store[4361]: not handling error download-failed for action download: failed to download https://odrs.gnome.org/1.0/reviews/api/ratings: SSL handshake failed
Jun 29 22:46:25 ty-virtual-machine snapd[752]: storehelpers.go:791: cannot refresh: snap has no updates available: "bare", "gtk-common-themes"
Jun 29 22:46:30 ty-virtual-machine PackageKit: get-updates transaction /16_ddaacbdd from uid 1000 finished with success after 5536ms
Jun 29 22:46:36 ty-virtual-machine update-notifier.desktop[7641]: /var/lib/apt/lists/lock:
Jun 29 22:46:44 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 29 22:46:44 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 29 22:46:45 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 29 22:46:45 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 29 22:46:46 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 29 22:46:46 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 29 22:47:07 ty-virtual-machine PackageKit: refresh-cache transaction /17_bdababad from uid 1000 finished with success after 26904ms
Jun 29 22:47:07 ty-virtual-machine snap-store[4361]: not handling error download-failed for action download: failed to download https://odrs.gnome.org/1.0/reviews/api/ratings: SSL handshake failed
Jun 29 22:47:08 ty-virtual-machine snapd[752]: storehelpers.go:791: cannot refresh: snap has no updates available: "bare", "gtk-common-themes"
Jun 29 22:47:13 ty-virtual-machine PackageKit: get-updates transaction /18_bcabeebe from uid 1000 finished with success after 5119ms
Jun 29 22:48:16 ty-virtual-machine kernel: [ 4189.351511] audit: type=1107 audit(1782787696.218:81): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.DBus.Properties" member="PropertiesChanged" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:48:16 ty-virtual-machine kernel: [ 4189.351511]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:48:27 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:48:29 ty-virtual-machine systemd[1]: message repeated 2 times: [ Reloading.]
Jun 29 22:48:29 ty-virtual-machine systemd[1]: Starting OpenBSD Secure Shell server...
Jun 29 22:48:29 ty-virtual-machine systemd[1]: Started OpenBSD Secure Shell server.
Jun 29 22:48:29 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:48:55 ty-virtual-machine kernel: [ 4228.231884] audit: type=1107 audit(1782787735.102:82): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.DBus.Properties" member="PropertiesChanged" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:48:55 ty-virtual-machine kernel: [ 4228.231884]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:49:38 ty-virtual-machine update-notifier.desktop[8906]: #015Reading package lists... 0%#015#015Reading package lists... 0%#015#015Reading package lists... 0%#015#015Reading package lists... 1%#015#015Reading package lists... 1%#015#015Reading package lists... 3%#015#015Reading package lists... 3%#015#015Reading package lists... 3%#015#015Reading package lists... 3%#015#015Reading package lists... 4%#015#015Reading package lists... 4%#015#015Reading package lists... 4%#015#015Reading package lists... 4%#015#015Reading package lists... 4%#015#015Reading package lists... 4%#015#015Reading package lists... 13%#015#015Reading package lists... 21%#015#015Reading package lists... 21%#015#015Reading package lists... 30%#015#015Reading package lists... 30%#015#015Reading package lists... 30%#015#015Reading package lists... 38%#015#015Reading package lists... 38%#015#015Reading package lists... 38%#015#015Reading package lists... 38%#015#015Reading package lists... 39%#015#015Reading package lists... 39%#015#015Reading package lists... 39%#015#015Reading package lists... 39%#015#015Reading package lists... 44%#015#015Reading package lists... 44%#015#015Reading package lists... 46%#015#015Reading package lists... 46%#015#015Reading package lists... 50%#015#015Reading package lists... 50%#015#015Reading package lists... 52%#015#015Reading package lists... 59%#015#015Reading package lists... 59%#015#015Reading package lists... 59%#015#015Reading package lists... 59%#015#015Reading package lists... 65%#015#015Reading package lists... 65%#015#015Reading package lists... 67%#015#015Reading package lists... 67%#015#015Reading package lists... 69%#015#015Reading package lists... 69%#015#015Reading package lists... 69%#015#015Reading package lists... 69%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 70%#015#015Reading package lists... 75%#015#015Reading package lists... 75%#015#015Reading package lists... 75%#015#015Reading package lists... 76%#015#015Reading package lists... 76%#015#015Reading package lists... 80%#015#015Reading package lists... 80%#015#015Reading package lists... 89%#015#015Reading package lists... 89%#015#015Reading package lists... 89%#015#015Reading package lists... 89%#015#015Reading package lists... 95%#015#015Reading package lists... 95%#015#015Reading package lists... 97%#015#015Reading package lists... 97%#015#015Reading package lists... 98%#015#015Reading package lists... 98%#015#015Reading package lists... 99%#015#015Reading package lists... 99%#015#015Reading package lists... 99%#015#015Reading package lists... 99%#015#015Reading package lists... 99%#015#015Reading package lists... 99%#015#015Reading package lists... 99%#015#015Reading package lists... 99%#015#015Reading package lists... Done
Jun 29 22:49:39 ty-virtual-machine update-notifier.desktop[8906]: #015Building dependency tree... 0%#015#015Building dependency tree... 0%#015#015Building dependency tree... 50%#015#015Building dependency tree... 50%#015#015Building dependency tree... 63%#015#015Building dependency tree... Done
Jun 29 22:49:39 ty-virtual-machine update-notifier.desktop[8906]: #015Reading state information... 0% #015#015Reading state information... 0%#015#015Reading state information... Done
Jun 29 22:49:49 ty-virtual-machine kernel: [ 4282.276690] e1000: ens33 NIC Link is Down
Jun 29 22:49:53 ty-virtual-machine kernel: [ 4286.309093] e1000: ens33 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: None
Jun 29 22:49:53 ty-virtual-machine NetworkManager[721]: <info>  [1782787793.1712] device (ens33): carrier: link connected
Jun 29 22:49:53 ty-virtual-machine NetworkManager[721]: <info>  [1782787793.1715] device (ens33): ip:dhcp4: restarting
Jun 29 22:49:53 ty-virtual-machine NetworkManager[721]: <info>  [1782787793.1848] dhcp4 (ens33): canceled DHCP transaction
Jun 29 22:49:53 ty-virtual-machine NetworkManager[721]: <info>  [1782787793.1849] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 29 22:49:53 ty-virtual-machine NetworkManager[721]: <info>  [1782787793.1849] dhcp4 (ens33): state changed no lease
Jun 29 22:49:53 ty-virtual-machine NetworkManager[721]: <info>  [1782787793.1850] dhcp4 (ens33): activation: beginning transaction (timeout in 45 seconds)
Jun 29 22:49:53 ty-virtual-machine NetworkManager[721]: <info>  [1782787793.2046] dhcp4 (ens33): state changed new lease, address=192.168.203.161
Jun 29 22:49:53 ty-virtual-machine dbus-daemon[719]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.6' (uid=0 pid=721 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 29 22:49:53 ty-virtual-machine systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 29 22:49:53 ty-virtual-machine dbus-daemon[719]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 29 22:49:53 ty-virtual-machine systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 29 22:50:03 ty-virtual-machine systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 29 22:50:08 ty-virtual-machine systemd-resolved[518]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.203.2.
Jun 29 22:50:46 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:50:47 ty-virtual-machine systemd[1]: message repeated 2 times: [ Reloading.]
Jun 29 22:55:50 ty-virtual-machine systemd[1350]: Started VTE child process 9052 launched by gnome-terminal-server process 2116.
Jun 29 22:56:02 ty-virtual-machine kernel: [ 4656.008893] audit: type=1107 audit(1782788162.858:83): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:56:02 ty-virtual-machine kernel: [ 4656.008893]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:56:02 ty-virtual-machine systemd[1]: Started Session 6 of User ty.
Jun 29 22:56:02 ty-virtual-machine systemd[1350]: Starting Notification regarding a new release of Ubuntu...
Jun 29 22:56:09 ty-virtual-machine systemd[1]: session-6.scope: Deactivated successfully.
Jun 29 22:56:09 ty-virtual-machine systemd[1]: session-6.scope: Consumed 5.449s CPU time.
Jun 29 22:56:09 ty-virtual-machine kernel: [ 4662.270220] audit: type=1107 audit(1782788169.118:84): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:56:09 ty-virtual-machine kernel: [ 4662.270220]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:56:10 ty-virtual-machine kernel: [ 4663.308111] audit: type=1107 audit(1782788170.158:85): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:56:10 ty-virtual-machine kernel: [ 4663.308111]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:56:10 ty-virtual-machine systemd[1]: Started Session 7 of User ty.
Jun 29 22:56:10 ty-virtual-machine systemd[1]: session-7.scope: Deactivated successfully.
Jun 29 22:56:10 ty-virtual-machine kernel: [ 4663.749260] audit: type=1107 audit(1782788170.598:86): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:56:10 ty-virtual-machine kernel: [ 4663.749260]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:56:43 ty-virtual-machine kernel: [ 4696.646045] audit: type=1107 audit(1782788203.494:87): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:56:43 ty-virtual-machine kernel: [ 4696.646045]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:56:43 ty-virtual-machine systemd[1]: Started Session 8 of User ty.
Jun 29 22:56:43 ty-virtual-machine systemd[1]: session-8.scope: Deactivated successfully.
Jun 29 22:56:43 ty-virtual-machine kernel: [ 4697.048525] audit: type=1107 audit(1782788203.894:88): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:56:43 ty-virtual-machine kernel: [ 4697.048525]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:56:53 ty-virtual-machine kernel: [ 4706.962217] audit: type=1107 audit(1782788213.810:89): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:56:53 ty-virtual-machine kernel: [ 4706.962217]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:56:53 ty-virtual-machine systemd[1]: Started Session 9 of User ty.
Jun 29 22:56:54 ty-virtual-machine systemd[1]: Starting Update APT News...
Jun 29 22:56:54 ty-virtual-machine systemd[1]: Starting Update the local ESM caches...
Jun 29 22:56:54 ty-virtual-machine systemd[1]: apt-news.service: Deactivated successfully.
Jun 29 22:56:54 ty-virtual-machine systemd[1]: Finished Update APT News.
Jun 29 22:56:56 ty-virtual-machine systemd[1]: esm-cache.service: Deactivated successfully.
Jun 29 22:56:56 ty-virtual-machine systemd[1]: Finished Update the local ESM caches.
Jun 29 22:57:31 ty-virtual-machine kernel: [ 4745.016155] audit: type=1107 audit(1782788251.867:90): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.DBus.Properties" member="PropertiesChanged" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:57:31 ty-virtual-machine kernel: [ 4745.016155]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:57:33 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:57:35 ty-virtual-machine systemd[1]: message repeated 2 times: [ Reloading.]
Jun 29 22:57:35 ty-virtual-machine systemd[1]: Starting Service for virtual machines hosted on VMware...
Jun 29 22:57:35 ty-virtual-machine systemd[1]: Started Service for virtual machines hosted on VMware.
Jun 29 22:57:36 ty-virtual-machine kernel: [ 4749.225321] NET: Registered PF_VSOCK protocol family
Jun 29 22:57:36 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:57:36 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:57:37 ty-virtual-machine systemd[1]: Started Authentication service for virtual machines hosted on VMware.
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: Pref_Init: Using '/etc/vmware-tools/vgauth.conf' as preferences filepath
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: Core dump limit set to -1
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: INIT SERVICE
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: Using '/var/lib/vmware/VGAuth/aliasStore' for alias store root directory
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: LoadCatalogAndSchema: Using '/etc/vmware-tools/vgauth/schemas' for SAML schemas
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: LoadPrefs: Allowing 300 of clock skew for SAML date validation
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: SAML_Init: Using xmlsec1 1.2.33 for XML signature support
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: ServiceNetworkCreateSocketDir: Created socket directory '/var/run/vmware'
Jun 29 22:57:37 ty-virtual-machine VGAuthService[10159]: BEGIN SERVICE
Jun 29 22:57:37 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:57:38 ty-virtual-machine systemd[1]: Reloading.
Jun 29 22:57:38 ty-virtual-machine systemd[1]: Mounting VMware vmblock fuse mount...
Jun 29 22:57:38 ty-virtual-machine systemd[1]: Mounted VMware vmblock fuse mount.
Jun 29 22:57:49 ty-virtual-machine check-new-release-gtk[9087]: Checking for a new Ubuntu release
Jun 29 22:57:49 ty-virtual-machine check-new-release-gtk[9087]: Please install all available updates for your release before upgrading.
Jun 29 22:57:49 ty-virtual-machine systemd[1350]: update-notifier-release.service: Main process exited, code=exited, status=1/FAILURE
Jun 29 22:57:49 ty-virtual-machine systemd[1350]: update-notifier-release.service: Failed with result 'exit-code'.
Jun 29 22:57:49 ty-virtual-machine systemd[1350]: Failed to start Notification regarding a new release of Ubuntu.
Jun 29 22:57:49 ty-virtual-machine systemd[1350]: update-notifier-release.service: Consumed 19.877s CPU time.
Jun 29 22:58:03 ty-virtual-machine kernel: [ 4776.587186] audit: type=1107 audit(1782788283.439:91): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.DBus.Properties" member="PropertiesChanged" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:58:03 ty-virtual-machine kernel: [ 4776.587186]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:58:03 ty-virtual-machine systemd[1]: session-9.scope: Deactivated successfully.
Jun 29 22:58:03 ty-virtual-machine systemd[1]: session-9.scope: Consumed 1min 964ms CPU time.
Jun 29 22:58:03 ty-virtual-machine kernel: [ 4776.681568] audit: type=1107 audit(1782788283.531:92): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:58:03 ty-virtual-machine kernel: [ 4776.681568]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:58:08 ty-virtual-machine kernel: [ 4781.804711] audit: type=1107 audit(1782788288.655:93): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:58:08 ty-virtual-machine kernel: [ 4781.804711]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:58:08 ty-virtual-machine systemd[1]: Started Session 10 of User ty.
Jun 29 22:58:09 ty-virtual-machine systemd[1]: session-10.scope: Deactivated successfully.
Jun 29 22:58:09 ty-virtual-machine kernel: [ 4782.358582] audit: type=1107 audit(1782788289.207:94): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:58:09 ty-virtual-machine kernel: [ 4782.358582]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:58:55 ty-virtual-machine kernel: [ 4828.378052] audit: type=1107 audit(1782788335.228:95): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:58:55 ty-virtual-machine kernel: [ 4828.378052]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:58:55 ty-virtual-machine systemd[1]: Started Session 11 of User ty.
Jun 29 22:58:55 ty-virtual-machine systemd[1]: session-11.scope: Deactivated successfully.
Jun 29 22:58:55 ty-virtual-machine kernel: [ 4828.599549] audit: type=1107 audit(1782788335.448:96): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:58:55 ty-virtual-machine kernel: [ 4828.599549]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:00 ty-virtual-machine kernel: [ 4834.070308] audit: type=1107 audit(1782788340.920:97): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:00 ty-virtual-machine kernel: [ 4834.070308]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:00 ty-virtual-machine systemd[1]: Started Session 12 of User ty.
Jun 29 22:59:01 ty-virtual-machine systemd[1]: session-12.scope: Deactivated successfully.
Jun 29 22:59:01 ty-virtual-machine kernel: [ 4834.471380] audit: type=1107 audit(1782788341.320:98): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:01 ty-virtual-machine kernel: [ 4834.471380]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:36 ty-virtual-machine kernel: [ 4869.463684] audit: type=1107 audit(1782788376.316:99): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:36 ty-virtual-machine kernel: [ 4869.463684]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:36 ty-virtual-machine systemd[1]: Started Session 13 of User ty.
Jun 29 22:59:36 ty-virtual-machine systemd[1]: session-13.scope: Deactivated successfully.
Jun 29 22:59:36 ty-virtual-machine kernel: [ 4869.678174] audit: type=1107 audit(1782788376.528:100): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:36 ty-virtual-machine kernel: [ 4869.678174]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:43 ty-virtual-machine kernel: [ 4876.687018] audit: type=1107 audit(1782788383.536:101): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:43 ty-virtual-machine kernel: [ 4876.687018]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:43 ty-virtual-machine systemd[1]: Started Session 14 of User ty.
Jun 29 22:59:43 ty-virtual-machine systemd[1]: session-14.scope: Deactivated successfully.
Jun 29 22:59:43 ty-virtual-machine kernel: [ 4877.096533] audit: type=1107 audit(1782788383.944:102): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:43 ty-virtual-machine kernel: [ 4877.096533]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:49 ty-virtual-machine kernel: [ 4882.378097] audit: type=1107 audit(1782788389.229:103): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:49 ty-virtual-machine kernel: [ 4882.378097]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:49 ty-virtual-machine systemd[1]: Started Session 15 of User ty.
Jun 29 22:59:49 ty-virtual-machine systemd[1]: session-15.scope: Deactivated successfully.
Jun 29 22:59:49 ty-virtual-machine kernel: [ 4882.606275] audit: type=1107 audit(1782788389.457:104): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:49 ty-virtual-machine kernel: [ 4882.606275]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:58 ty-virtual-machine kernel: [ 4891.203620] audit: type=1107 audit(1782788398.053:105): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:58 ty-virtual-machine kernel: [ 4891.203620]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 22:59:58 ty-virtual-machine systemd[1]: Started Session 16 of User ty.
Jun 29 22:59:58 ty-virtual-machine systemd[1]: session-16.scope: Deactivated successfully.
Jun 29 22:59:58 ty-virtual-machine kernel: [ 4891.700122] audit: type=1107 audit(1782788398.549:106): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 22:59:58 ty-virtual-machine kernel: [ 4891.700122]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:01:12 ty-virtual-machine kernel: [ 4965.657977] audit: type=1107 audit(1782788472.510:107): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 23:01:12 ty-virtual-machine kernel: [ 4965.657977]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:01:12 ty-virtual-machine systemd[1]: Started Session 17 of User ty.
Jun 29 23:01:12 ty-virtual-machine systemd[1]: session-17.scope: Deactivated successfully.
Jun 29 23:01:12 ty-virtual-machine kernel: [ 4965.900444] audit: type=1107 audit(1782788472.754:108): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 23:01:12 ty-virtual-machine kernel: [ 4965.900444]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:01:37 ty-virtual-machine kernel: [ 4990.659390] audit: type=1107 audit(1782788497.510:109): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 23:01:37 ty-virtual-machine kernel: [ 4990.659390]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:01:37 ty-virtual-machine systemd[1]: Started Session 18 of User ty.
Jun 29 23:01:37 ty-virtual-machine systemd[1]: session-18.scope: Deactivated successfully.
Jun 29 23:01:37 ty-virtual-machine kernel: [ 4990.909590] audit: type=1107 audit(1782788497.762:110): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 23:01:37 ty-virtual-machine kernel: [ 4990.909590]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:02:27 ty-virtual-machine kernel: [ 5040.275610] audit: type=1107 audit(1782788547.126:111): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 23:02:27 ty-virtual-machine kernel: [ 5040.275610]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:02:27 ty-virtual-machine systemd[1]: Started Session 19 of User ty.
Jun 29 23:02:27 ty-virtual-machine systemd[1]: session-19.scope: Deactivated successfully.
Jun 29 23:02:27 ty-virtual-machine kernel: [ 5040.563480] audit: type=1107 audit(1782788547.414:112): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionRemoved" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 23:02:27 ty-virtual-machine kernel: [ 5040.563480]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:03:21 ty-virtual-machine kernel: [ 5095.118451] audit: type=1107 audit(1782788601.969:113): pid=719 uid=102 auid=4294967295 ses=4294967295 subj=unconfined msg='apparmor="DENIED" operation="dbus_signal"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="SessionNew" name=":1.12" mask="receive" pid=4640 label="snap.firefox.firefox" peer_pid=760 peer_label="unconfined"
Jun 29 23:03:21 ty-virtual-machine kernel: [ 5095.118451]  exe="/usr/bin/dbus-daemon" sauid=102 hostname=? addr=? terminal=?'
Jun 29 23:03:21 ty-virtual-machine systemd[1]: Started Session 20 of User ty.

```
