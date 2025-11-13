import Chart from "@/components/Chart";
import AiSummaryPanel from "@/components/AiSummaryPanel";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Chart />
      <div className="w-full max-w-md">
        <AiSummaryPanel />
      </div>
    </main>
  );
}
