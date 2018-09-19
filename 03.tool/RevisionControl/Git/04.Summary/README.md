# 总结

* 1.push错误或者提交子模块仓库
    * 解决方案:
        * 1.清空暂存区
        git rm -r --cached .
        * 2.重新提交
            ```bash
            git add .
            git commit -m ".gitignore is now working"
            git push
             ```

* 2.LF would be replaced by CRLF
    * 解决方案:
        * 1.取消转换
            ```bash
            git config –global core.autocrlf false
            ```
