# Python / JSON TODOs

# Install

```bash
$ mkvirtualenv todos -p /usr/bin/python3
$ pip install -r requirements.txt
```

# Change branches to students-tasks

```bash
$ git checkout -b students-tasks origin/students-tasks
```

# Usage

**General:**

```bash
$ python main.py --help
$ python main.py --debug
```

**List todos**
```bash
$ python main.py list
$ python main.py list -s pending
$ python main.py list -s done
$ python main.py list -s allmak
```


**Create todos**
```bash
$ python main.py create "My TODO Task"
$ python main.py create "My TODO Task" -d "Much description, wow"
$ python main.py create "My TODO Task" -d "Much description, wow" -p "2018-03-05"
$ python main.py create "My TODO Task" -d "Much description, wow" -p "2018-03-05 19:25:33"
```

**Complete task**
```bash
$ python main.py complete "My TODO Task"
$ python main.py complete 1  # by order/id
```

### Student's Tasks

The branch `students-tasks` contains some unsolved pieces of the code. Don't worry that your instructor is supposed to go over all this during class. But as a extra reference, here's what you'll find:

##### Main tests

There are 5 tests that need fixing. You can find them in `tests.py` with comments similar to `# FIXME: Test`. To run those tests you can use some make commands that we've created. For example:

```bash
$ make test_1
$ make test_2
$ make test_3 #... etc
```

There are also two more tasks that show extra info

```bash
$ make test  # Runs ALL the tests
$ make test_summary # Just prints a quick summary of the tests that are failing
```

##### Optional exercises

There are two optional tests that can be run with:

```bash
$ make optional_test_1
$ make optional_test_2
```
