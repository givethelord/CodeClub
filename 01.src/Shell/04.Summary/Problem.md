# 问题

1. shell对数组支持不好，如果直接使用for循环遍历数组，很容易把某个包含空格的元素当成多个元素。所以建议遍历元素位置
    ```bash
    #!/usr/bin/env bash
    arr=(1 2 3 4 5)
    arr=(${arr[*]} "aa bb")
    n_arr=${#arr[@]}
    for((i=0;i<$n_arr;i++))
    do
        elem=${arr[$i]}
        echo "$i:$elem"
    done
    ```

2. while中使用重定向机制，data文件中的形象都已经读入且重定向给了整个while语句，所以当我们使用while语句中再一次调用read语句，就会读取到下一条记录。ssh语句会读取输入的所有语句导致wwhile语句结束。所以while循环里面如果有ssh命令需要重定向输入方向.
    ```bash
    #!/usr/bin/env bash
    while read Line
    do
        ssh ip "$Line"  < /dev/null
    done < data
