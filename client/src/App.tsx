
import { useState } from 'react';
import './App.css'

function App() {
  const [playlist, setPlaylist] = useState<string>('');
  const sendLink = async (e, link:string) => {
    e.preventDefault();
    try {
      const res = await fetch('/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body:JSON.stringify({playlistLink: link})
      })
      if (!res.ok) {
        throw new Error('HTTP Error: ' + res.status);
      }
    }
    catch (error){
      console.log("error:", error)
    }
  }
  return (
    <form onSubmit={(e) => sendLink(e,playlist)}>
      <input type="text" placeholder="spotify link" onChange={(e) => {setPlaylist(e.target.value)}}/>
      <input type="submit" />
    </form>
  )
}

export default App
