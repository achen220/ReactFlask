
import { useState } from 'react';
import './App.css'

function App() {
  const sendLink = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('/api', {
        method: 'GET',
        headers: {'Content-Type': 'application/json'}
      })
      const resBlob = await res.blob();
      // Create a link element
      const link = document.createElement('a');

      // Create a Blob URL from the response blob
      const blobUrl = URL.createObjectURL(resBlob);

      // Set the link's href to the Blob URL
      link.href = blobUrl;

      // Set the link's download attribute with the desired file name
      link.download = 'example.xlsx';

      // Append the link to the document
      document.body.appendChild(link);

      // Trigger a click on the link to initiate the download
      link.click();

      // Remove the link from the document
      document.body.removeChild(link);

      // Revoke the Blob URL to free up resources
      URL.revokeObjectURL(blobUrl);
      if (!res.ok) {
        throw new Error('HTTP Error: ' + res.status);
      }
    }
    catch (error){
      console.log("error:", error)
    }
  }
  return (
    <form onSubmit={(e) => sendLink(e)}>
      <input type="submit" />
    </form>
  )
}

export default App
