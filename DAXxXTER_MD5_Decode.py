#!usr/bin/perl
# DAXxXTER MD5 Cracker v1.2
# coded by : rio suyanto
# rio_suyanto00@yahoo.co.id

system('cls');
system( 'title DAXxXTER MD5 Cracker v1.2');
use strict;
use warnings;
use Digest::MD5 qw(md5_hex);

sub usage(){

print <<EOF; 

-----------------------------------------
| DAXxXTER MD5 Cracker v1.8             | trimakasih kepada tuhan yesus kristus
| ceded by : rio suyanto                |     karna memberikan saya hikmat
| blog     : rio-suyanto.blogspot.com   |        kekuatan dan kesehatan
-----------------------------------------      Semoga ini dapat membantu.

EOF
print "Contoh: DAXxXTER_MD5_Decode.py <hash-file> <wordlist>\n";


}

my $hashplace=shift;
my $wlistplace=shift;

if(!$wlistplace){
   usage();
   exit;
}
   open(HASH,$hashplace) || die "Password hash tak dapat di buka : $!\n";
      chomp(my $hash=<HASH>);
   close(HASH);

if(length($hash)!=32){
   die "\t$hash Bukan md5-hash..!!\n";
}
if($hash !~ /\d|[a-f]{32}/g){
   die "\t$hash Bukan md5-hash..!!\n";
}
   open(WLIST,$wlistplace) || die "Tak dapat membuka wordlist wordlist : $!\n";

while(<WLIST>){
   chomp($_);
   chomp(my $md5=md5_hex($_));
   print "$md5 mencocokan => $hash\n";
   if($md5 eq $hash){
   print "\n";
      die "\t                Hash Berhasil di crack!\n\n\t$hash == $_\n\n";
   }
}
close(WLIST);

print "Hash tak di temukan di wordlist\n"; 
