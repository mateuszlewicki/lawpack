#! /usr/bin/perl

sub BuildDefault{

    my $SCSD = BuildSCSD();
    my $shell = $ENV{'SHELL'};
    my $lawpackdir = "/lawtrans/a699323";
    my $logfile = "lawpack.log";
    my $insfile = "input.xml";
    my $default = << "EOM";
<config>
    <DEBUG_MODE>1</DEBUG_MODE>
    <SHELL>$shell</SHELL>
    <LAWPACKDIR>$lawpackdir</LAWPACKDIR>
    <LOG_FILE>$lawpackdir/$logile</LOG_FILE>
    <INS_FILE>$lawpackdir/$insfile</INS_FILE>
    <CLANG>SCHLUM2</CLANG>
    <SCSD>$SCSD</SCSD>
    <CTC></CTC>
</config>
EOM

    print($default);

}

sub BuildSCSD{

    my %scsd = ();

    my $lawdir = $ENV{'LAWDIR'};

    my $WINTMP = 'C:\cygwin64\lawson\l9qa\law\qa91';
    $lawdir=$WINTMP;
    # my $lsdir =
    print($ENV{USERNAME});
    open (DIR , $lawdir) or die $!;

    while (my $file = readdir(DIR)){
        next if ($file !~ m/^[A-Za-z]{2}src$/);

        $scsd{substr($file,0,2)} = $file;

    }
    return $scsd
}


BuildDefault();
