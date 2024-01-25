import { Button, Stack, TextField, Typography } from '@mui/material'



export default async function Home() {
  // fetchを使用する例
  async function fetchItem() {
    try {
      const response = await fetch(`http://backend:8000/tasks`);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Database Error:', error);
      throw new Error('Failed to fetch total number of invoices.');
    }
  }

  const tasks = await fetchItem();
  console.log(tasks);
  

  return (
    <main>
      <Stack height="100lvh" justifyContent="center" alignItems="center" gap="32px">
        <Typography id="login_heading" variant="h1" fontSize="1.5rem">タスクを入力してネ</Typography>
        <Stack component="form" width={560} gap="24px" aria-labelledby="login_heading">
          <TextField label="タスク" />
          <Button variant="contained">決定</Button>
        </Stack>
        {tasks.map((task:any) => (
          <div>
            {task.title}
          </div> 
        ))}
      </Stack>
    </main>
  )
}
