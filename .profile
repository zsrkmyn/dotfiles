[[ `which systemctl` ]] && systemctl --user import-environment PATH

export MAKEFLAGS=-j4
export PAGER='less -FXMr'
export PATH=$PATH:~/.bin

if [[ `which nvim` ]]; then
	EDITOR=nvim
	alias vi=nvim
	alias vim=nvim
else
	EDITOR=vim
fi
export EDITOR

# for ccache
export PATH=/usr/lib64/ccache/bin/:/usr/lib/ccache/bin/:$PATH
export CCACHE_DIR=/tmp/.ccache
