class Git:
    add = "adding"
    commit = "committing"
    push = "pushing"
    merge = "merging"

    def run_merge(self):
        print(self.merge)

    def run_commit(self):
        print(self.commit)

    def run_add(self):
        print(self.add)

    def run_push(self):
        print(self.push)

git_instance = Git()

while True:
    user_input = input('''\nChoose one oof the following:
1. add
2. commit
3. push
4. merge
5. exit
: ''')
    if(user_input == "1"):
        Git.run_add(git_instance)
    elif(user_input == "2"):
        Git.run_commit(git_instance)
    elif(user_input == "3"):
        Git.run_push(git_instance)
    elif(user_input == "4"):
        Git.run_merge(git_instance)
    elif(user_input == "5"):
        break
    else:
        print("invalid option!")
print("GoodBye!")