for i in \
	.inputrc .ipython .msmtprc .mutt .offlineimap.d \
	.profile .tmux.conf .toprc .urlview .zshrc .Xmodmap
do
	ln -s "$(pwd)/$i" ~/
done

[[ -d ~/.config ]] || mkdir ~/.config
for i in i3 i3status compton.conf; do
	ln -s "$(pwd)/$i" ~/.config/
done
