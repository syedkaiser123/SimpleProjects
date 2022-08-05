#!/usr/bin/bash

git branch
"$(git log -n 2 --pretty=format:"%H" > log.txt)"

# python commit-diff-extractor.py > tempfile.txt
# readarray commits < tempfile.txt
# rm tempfile.txt
# echo "$commits"

declare -a last_n_commits
END=2
for j in $(seq 1 $END)
do
    if [ "$j" == 1 ]
    then
        # echo "inside if"
        last_n_commits[0]="$(git rev-parse HEAD~0)" #ultimate/last commit
    else
        # echo "inside else"
        last_n_commits[1]="$(git rev-parse HEAD~1)" #pinultimate/2nd-last commit
    fi
done

# echo ${#last_n_commits}   #length of array
echo "last 2 commmits: ${last_n_commits[@]}"
echo "files changed: "$(git diff --name-only ${last_n_commits[0]} ${colast_n_commitsmmits[1]})""
# echo "$(git diff ${last_n_commits[0]} ${colast_n_commitsmmits[1]} | grep '^[+-][^+-]' | grep -Ev "^(--- a/|\+\+\+ b/)")"
# "$(git diff ${last_n_commits[0]} ${colast_n_commitsmmits[1]} | grep '^[+-][^+-]' | grep -Ev "^(--- a/|\+\+\+ b/)" > output.txt)"
# "$(git diff > ouput.txt)"
# echo "$(git log -n 2 --pretty=format:"%H")" > log.txt

############################################
# commits="$(python - << EOF
# commits = []
# with open('log.txt', 'r') as f:
#     temp = f.readlines()
#     for i in temp:
#         if '\n' in i:
#             commits.append((i.replace('\n','')))
#         else:
#             commits.append(i)
# print(commits)
# EOF
# )"
############################################


echo "$(git diff | gawk '
  match($0,"^@@ -([0-9]+),([0-9]+) [+]([0-9]+),([0-9]+) @@",a){
    left=a[1]
    ll=length(a[2])
    right=a[3]
    rl=length(a[4])
  }
  /^(---|\+\+\+|[^-+ ])/{ print;next }
  { line=substr($0,2) }
  /^[-]/{ printf "-%"ll"s %"rl"s:%s\n",left++,""     ,line;next }
  /^[+]/{ printf "+%"ll"s %"rl"s:%s\n",""    ,right++,line;next }
        { printf " %"ll"s %"rl"s:%s\n",left++,right++,line }
'
)"

"$(git diff | gawk '
  match($0,"^@@ -([0-9]+),([0-9]+) [+]([0-9]+),([0-9]+) @@",a){
    left=a[1]
    ll=length(a[2])
    right=a[3]
    rl=length(a[4])
  }
  /^(---|\+\+\+|[^-+ ])/{ print;next }
  { line=substr($0,2) }
  /^[-]/{ printf "-%"ll"s %"rl"s:%s\n",left++,""     ,line;next }
  /^[+]/{ printf "+%"ll"s %"rl"s:%s\n",""    ,right++,line;next }
        { printf " %"ll"s %"rl"s:%s\n",left++,right++,line }
' | grep '^[+-][^+-]' | grep -Ev "^(--- a/|\+\+\+ b/)" > output.txt)"

eval "$(rm -rf output.txt)"
eval "$(rm -rf log.txt)"