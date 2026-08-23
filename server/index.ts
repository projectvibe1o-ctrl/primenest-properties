import express from "express";
import { createServer } from "http";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function startServer() {
  const app = express();
  const server = createServer(app);
  const staticPath = path.resolve(__dirname, "public");
  const indexPath = path.join(staticPath, "index.html");

  app.use(express.static(staticPath));

  // Express 5 no longer accepts the string wildcard "*" here.
  // A regular-expression fallback keeps client-side routes working.
  app.get(/.*/, (_req, res) => {
    res.sendFile(indexPath);
  });

  const port = Number(process.env.PORT) || 3000;
  server.listen(port, () => {
    console.log(`PrimeNest server listening on port ${port}`);
  });
}

startServer().catch((error) => {
  console.error("PrimeNest server failed to start", error);
  process.exitCode = 1;
});
