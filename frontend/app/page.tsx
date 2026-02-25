import fs from "fs";
import path from "path";

export default function Home() {
  const filePath = path.join(process.cwd(), "../backend/data/ideas.json");
  const data = JSON.parse(fs.readFileSync(filePath, "utf8"));

  return (
    <main style={{ padding: 40 }}>
      <h1>AI Money Ideas</h1>
      {data.ideas?.map((idea: any, i: number) => (
        <div key={i} style={{ border: "1px solid #ccc", margin: 20, padding: 20 }}>
          <h2>{idea.title}</h2>
          <p>{idea.strategy}</p>
          <ul>
            {idea.execution_steps.map((s: string, j: number) => (
              <li key={j}>{s}</li>
            ))}
          </ul>
          <p>Difficulty: {idea.difficulty}</p>
        </div>
      ))}
    </main>
  );
}