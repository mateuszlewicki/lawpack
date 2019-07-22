#! /usr/bin/perl

use Path::Tiny;

if (scalar @ARGV == 0){
	print("Provide package number \nexample: finder.pl pkg_num\n");
	exit 1;
}
my $pkg_name = @ARGV[0];

my @dirs = ();
my @pkg_loc = ();
my $pkgdir = '/lawtrans';

my $WINTMP = 'C:\cygwin64\lawson\l9qa\law\qa91';
# $lawdir=$WINTMP;
sub walk{
    my $dir= path($_[0]);
    my $match = $_[1];

    my @dirs = ();

    my $iter = $dir->iterator;

    while (my $file = $iter->()) {

        next if ($file !~ m/^.*\/$match.*$/);


        push @dirs, $file;


    }

    return @dirs;
}

my @dirs = walk($pkgdir, "ALM");

my @dbdirs = ();
foreach my $dir (@dirs) {
    push @dbdirs, walk($dir,"dbfix");
    push @dbdirs, walk($dir,"datafix");

}

push @dirs, @dbdirs;

foreach $dir (@dirs){

    push @pkg_loc, walk($dir,$pkg_name);


}

if (scalar @pkg_loc == 0){
    print("Package $pkg_name not found\n");
    exit 2;
}

#TODO: RETURN
foreach $f (@pkg_loc){
print "$f\n";
}
