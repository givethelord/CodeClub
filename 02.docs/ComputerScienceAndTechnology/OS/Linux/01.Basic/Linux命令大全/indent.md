# Linux indent命令
[返回Linux 命令目录](11.Linux命令大全.md)

Linux indent命令用于调整C原始代码文件的格式。

indent可辨识C的原始代码文件，并加以格式化，以方便程序设计师阅读。

## 语法
```bash
indent [参数][源文件] 或 indent [参数][源文件][-o 目标文件]
```
参数：
* -bad或--blank-lines-after-declarations 　在声明区段或加上空白行。
* -bap或--blank-lines-after-procedures 　在程序或加上空白行。
* -bbb或--blank-lines-after-block-comments 　在注释区段后加上空白行。
* -bc或--blank-lines-after-commas 　在声明区段中，若出现逗号即换行。
* -bl或--braces-after-if-line 　if(或是else,for等等)与后面执行区段的"{"不同行，且"}"自成一行。
* -bli<缩排格数>或--brace-indent<缩排格数> 　设置{ }缩排的格数。
* -br或--braces-on-if-line 　if(或是else,for等等)与后面执行跛段的"{"不同行，且"}"自成一行。
* -bs或--blank-before-sizeof 　在sizeof之后空一格。
* -c<栏数>或--comment-indentation<栏数> 　将注释置于程序码右侧指定的栏位。
* -cd<栏数>或--declaration-comment-column<栏数> 　将注释置于声明右侧指定的栏位。
* -cdb或--comment-delimiters-on-blank-lines 　注释符号自成一行。
* -ce或--cuddle-else 　将else置于"}"(if执行区段的结尾)之后。
* -ci<缩排格数>或--continuation-indentation<缩排格数> 　叙述过长而换行时，指定换行后缩排的格数。
* -cli<缩排格数>或--case-indentation-<缩排格数> 　使用case时，switch缩排的格数。
* -cp<栏数>或-else-endif-column<栏数> 　将注释置于else与elseif叙述右侧定的栏位。
* -cs或--space-after-cast 　在cast之后空一格。
* -d<缩排格数>或-line-comments-indentation<缩排格数> 　针对不是放在程序码右侧的注释，设置其缩排格数。
* -di<栏数>或--declaration-indentation<栏数> 　将声明区段的变量置于指定的栏位。
* -fc1或--format-first-column-comments 　针对放在每行最前端的注释，设置其格式。
* -fca或--format-all-comments 　设置所有注释的格式。
* -gnu或--gnu-style 　指定使用GNU的格式，此为预设值。
* -i<格数>或--indent-level<格数> 　设置缩排的格数。
* -ip<格数>或--parameter-indentation<格数> 　设置参数的缩排格数。
* -kr或--k-and-r-style 　指定使用Kernighan&Ritchie的格式。
* -lp或--continue-at-parentheses 　叙述过长而换行，且叙述中包含了括弧时，将括弧中的每行起始栏位内容垂直对其排列。
* -nbad或--no-blank-lines-after-declarations 　在声明区段后不要加上空白行。
* -nbap或--no-blank-lines-after-procedures 　在程序后不要加上空白行。
* -nbbb或--no-blank-lines-after-block-comments 　在注释区段后不要加上空白行。
* -nbc或--no-blank-lines-after-commas 　在声明区段中，即使出现逗号，仍旧不要换行。
* -ncdb或--no-comment-delimiters-on-blank-lines 　注释符号不要自成一行。
* -nce或--dont-cuddle-else 　不要将else置于"}"之后。
* -ncs或--no-space-after-casts 　不要在cast之后空一格。
* -nfc1或--dont-format-first-column-comments 　不要格式化放在每行最前端的注释。
* -nfca或--dont-format-comments 　不要格式化任何的注释。
* -nip或--no-parameter-indentation 　参数不要缩排。
* -nlp或--dont-line-up-parentheses 　叙述过长而换行，且叙述中包含了括弧时，不用将括弧中的每行起始栏位垂直对其排列。
* -npcs或--no-space-after-function-call-names 　在调用的函数名称之后，不要加上空格。
* -npro或--ignore-profile 　不要读取indent的配置文件.indent.pro。
* -npsl或--dont-break-procedure-type 　程序类型与程序名称放在同一行。
* -nsc或--dont-star-comments 　注解左侧不要加上星号(*)。
* -nsob或--leave-optional-semicolon 　不用处理多余的空白行。
* -nss或--dont-space-special-semicolon 　若for或while区段仅有一行时，在分号前不加上空格。
* -nv或--no-verbosity 　不显示详细的信息。
* -orig或--original 　使用Berkeley的格式。
* -pcs或--space-after-procedure-calls 　在调用的函数名称与"{"之间加上空格。
* -psl或--procnames-start-lines 　程序类型置于程序名称的前一行。
* -sc或--start-left-side-of-comments 　在每行注释左侧加上星号(*)。
* -sob或--swallow-optional-blank-lines 　删除多余的空白行。
* -ss或--space-special-semicolon 　若for或swile区段今有一行时，在分号前加上空格。
* -st或--standard-output 　将结果显示在标准输出设备。
* -T 　数据类型名称缩排。
* -ts<格数>或--tab-size<格数> 　设置tab的长度。
* -v或--verbose 　执行时显示详细的信息。
* -version 　显示版本信息。

## Indent代码格式化说明

|使用的indent参数|	值|	含义
---------|------|------
--blank-lines-after-declarations	|	bad	|	变量声明后加空行
--blank-lines-after-procedures	|	bap	|	函数结束后加空行
--blank-lines-before-block-comments	|	bbb	|	块注释前加空行
--break-before-boolean-operator	|	bbo	|	较长的行，在逻辑运算符前分行
--blank-lines-after-commas	|	nbc	|	变量声明中，逗号分隔的变量不分行
--braces-after-if-line	|	bl	|	"if"和"{"分做两行
--brace-indent 0	|	bli0	|	"{"不继续缩进
--braces-after-struct-decl-line	|	bls	|	定义结构，"struct"和"{"分行
--comment-indentationn	|	c33	|	语句后注释开始于行33
--declaration-comment-columnn	|	cd33	|	变量声明后注释开始于行33
--comment-delimiters-on-blank-lines	|	ncdb	|	不将单行注释变为块注释
--cuddle-do-while	|	ncdw	|	"do --- while"的"while"和其前面的"}"另起一行
--cuddle-else	|	nce	|	"else"和其前面的"}"另起一行
--case-indentation 0	|	cli0	|	switch中的case语句所进0个空格
--else-endif-columnn	|	cp33	|	#else, #endif后面的注释开始于行33
--space-after-cast	|	cs	|	在类型转换后面加空格
--line-comments-indentation n	|	d0	|	单行注释（不从1列开始的），不向左缩进
--break-function-decl-args	|	nbfda	|	关闭：函数的参数一个一行
--declaration-indentationn	|	di2	|	变量声明，变量开始于2行，即不必对齐
--format-first-column-comments	|	nfc1	|	不格式化起于第一行的注释
--format-all-comments	|	nfca	|	不开启全部格式化注释的开关
--honour-newlines	|	hnl	|	Prefer to break long lines at the position of newlines in the input.
--indent-leveln	|	i4	|	设置缩进多少字符，如果为tab的整数倍，用tab来缩进，否则用空格填充。
--parameter-indentationn	|	ip5	|	旧风格的函数定义中参数说明缩进5个空格
--line-length 75	|	l75	|	非注释行最长75
--continue-at-parentheses	|	lp	|	续行从上一行出现的括号开始
--space-after-procedure-calls	|	pcs	|	函数和"("之间插入一个空格
--space-after-parentheses	|	nprs	|	在"（"后"）"前不插入空格
--procnames-start-lines	|	psl	|	将函数名和返回类型放在两行定义
--space-after-for	|	saf	|	for后面有空格
--space-after-if	|	sai	|	if后面有空格
--space-after-while	|	saw	|	while后面有空格
--start-left-side-of-comments	|	nsc	|	不在生成的块注释中加*
--swallow-optional-blank-lines	|	nsob	|	不去掉可添加的空行
--space-special-semicolon	|	nss	|	一行的for或while语句，在";"前不加空。
--tab-size	|	ts4	|	一个tab为4个空格（要能整除"-in"）
--use-tabs	|	ut	|	使用tab来缩进