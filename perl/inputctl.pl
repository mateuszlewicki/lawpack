#! /usr/bin/perl

use Path::Tiny;

if (scalar @ARGV == 0){
	print("Provide package catalog \nexample: inputctl.pl /lawtrans/ALM_RELEASE/pkg_num\n");
	exit 3;
}

my $pkg_dir = @ARGV[0];
my @dir_files = ();


sub walk{
    my $dir= path($_[0]);
    # my $match = $_[1];

    my @dirs = ();

    my $iter = $dir->iterator;

    while (my $file = $iter->()) {

        push @dirs, $file;

    }

    return @dirs;
}

@dir_files = walk($pkg_dir);



foreach my $file (@dir_files){

    print ("$file\n") if ($file =~ m/.*\.sql$/);

}
# print "@dir_files\n";
