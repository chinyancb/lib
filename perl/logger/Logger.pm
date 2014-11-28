package Logger;

use strict;
use warnings;
use Carp qw(croak);

# ログレベルに応じた文言
use constant {
	FATAL => 'fatal',
	ERROR => 'error',
	WARN => 'warn',
	INFO => 'info',
	DEBUG => 'debug',
	TRACE => 'trace',
};

# ファイルハンドラ
my $LOGFH;

##
# new
# @access:public
# @param:path => ログ出力先パス
# @return:nomal => 1
#        :abnomal => 強制終了
sub new {

	# 引数にファイルのパスがなければ強制終了
	croak '[ERROR] invalid argument.' if @_ != 2;	

	my $class = shift;
	my $path = shift;

	my $self = {path => $path};

	# ファイルopen
	open $LOGFH, ">> $self->{path}" or croak "[ERROR] Failed to open : $self->{path}";

	bless $self, $class;
}

1;
