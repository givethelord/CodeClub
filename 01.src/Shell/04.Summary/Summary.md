# 总结

* 1.命令运行符号& ; &&区别

    * command1&command2&command3:三个命令同时执行
    * command1;command2;command3:不管前面命令执行成功没有，后面的命令继续执行 
    * command1&&command2:只有前面命令执行成功，后面命令才继续执行