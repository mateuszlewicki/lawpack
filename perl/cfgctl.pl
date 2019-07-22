#! /usr/bin/perl

use Path::Tiny;

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
    <LOG_FILE>$lawpackdir/$logfile</LOG_FILE>
    <INS_FILE>$lawpackdir/$insfile</INS_FILE>
    <CLANG>SCHLUM2</CLANG>
    <SCSD>$SCSD </SCSD>
    <CTC></CTC>
</config>
EOM

    print($default);

}

sub BuildSCSD{

    my @scsd = ();

    my $lawdir = $ENV{'LAWDIR'}.'/'.$ENV{'XXPDL'};

    my $WINTMP = 'C:\cygwin64\lawson\l9qa\law\qa91';
    # $lawdir=$WINTMP;

    my $dir = path($lawdir);
    my $iter = $dir->iterator;

    while (my $file = $iter->()) {


        next if ($file !~ m/^.*[A-Za-z]{2}src$/);


        push @scsd, $file;


    }

    my $xmlstr="\n";
    foreach $item (@scsd){
        my $sc = substr $item, -5,2;
		my $sd = substr $item, -5,5;
		$sc = uc $sc;
        $xmlstr.="\t\<$sc\>\$LAWDIR\/\$XXPDL\/$sd\<\/$sc>\n";

    }
    return $xmlstr;
}
#TODO: save to file
#TODO: clasified to copy 

BuildDefault();
