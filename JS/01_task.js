// Node.js v20 has build in fetch without need to import 
// node --env-file=../.env 01_task.js <<-- in order to use env variables
// helloapi 
const taskNameUrl = 'https://tasks.aidevs.pl/token/helloapi';
const apikey = process.env.AI_DEVS_2_API_KEY || '';

async function getTaskToken() {
  const response = await fetch(taskNameUrl, {
    method: 'POST',
    body: JSON.stringify({ apikey: apikey }),
  });
  const data = await response.json();
  console.log(data);
  return data;
};

async function getTaskName(token) {
  const response = await fetch(`https://tasks.aidevs.pl/task/${token}`, {
    method: 'GET'
  });
  const data = await response.json();
  console.log(data);
  return data;
}

async function submitResponse (token, answer) {
  const response = await fetch(`https://tasks.aidevs.pl/answer/${token}`, {
    method: 'POST',
    body: JSON.stringify({answer: answer}),
  });
  const data = await response.json();
  console.log(data);
  return data;
}
const  firstTask = async () => {
  try {
  const { token = ''} = await getTaskToken();
  
  const {cookie = ''} = await getTaskName(token);
  console.log(cookie);

  submitResponse(token,cookie);

} catch (error) {
  console.error('Error:', error);
}

  console.log('first task');

}

firstTask();