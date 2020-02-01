
sub restart_ap(){
	my $pid_string = qx/sudo ps -e |grep create_ap/;
	my ($kill_num) = $pid_string =~ /(\d+)/;
	system "sudo kill $kill_num";
	system "sudo rm ~/.ap_log.txt && sudo create_ap -m nat --daemon --no-virt wlan0 eth0 MyWifi MyPassPhrase >~/.ap_log.txt"
}

while (true){
	sleep(345600)
	restart_ap()
}
