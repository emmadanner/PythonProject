import argparse
from tasks import add_task
from tasks import list_tasks
from tasks import complete_task
from tasks import delete_task

def main():
  parser = argparse.ArgumentParser(description="Task list manipulation script")
  # Argument to show tasks on the list
  parser.add_argument("--list", action="store_true", help="List tasks")
  # Argument to add tasks to the list
  parser.add_argument("--add", nargs=2, metavar=("NAME", "DESCRIPTION"), help="Add a task to the list")
  # Argument to delete tasks from the list
  parser.add_argument("--delete", type=int, metavar="TASK_NUMBER", help="Delete a task, list the task number")
  # Argument to mark tasks on the list as completed
  parser.add_argument("--complete", type=int, metavar="TASK_NUMBER", help="Mark task as completed, list the task number")

  args = parser.parse_args()

  if args.list:
    list_tasks()
  elif args.add:
    name, description = args.add
    add_task(name, description)
  elif args.delete:
    delete_task(args.delete)
  elif args.complete:
    complete_task(args.complete)

if __name__ == "__main__":
    main()