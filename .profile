# old zsh doesn't support [[ `cmd` ]] expr
which systemctl &> /dev/null
[[ $? -eq 0 ]] && systemctl --user import-environment PATH

export MAKEFLAGS=-j4
export PAGER='less -FXMr'
export PATH=$PATH:~/.bin

which nvim &> /dev/null
if [[ $? -eq 0 ]]; then
	EDITOR=nvim
	alias vi=nvim
	alias vim=nvim
else
	EDITOR=vim
fi
export EDITOR

[[ -f ~/.profile.extra ]] && . ~/.profile.extra

# for ccache
export PATH=/usr/lib64/ccache/bin/:/usr/lib/ccache/bin/:$PATH
export CCACHE_DIR=/tmp/.ccache
