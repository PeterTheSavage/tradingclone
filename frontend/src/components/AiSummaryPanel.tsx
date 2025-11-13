"use client";

import { useState } from "react";

const AiSummaryPanel = () => {
  const [summary, setSummary] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const fetchSummary = async () => {
    setIsLoading(true);
    setSummary("");
    try {
      // In a real application, you would fetch the chart data here.
      // For now, we'll use an empty array.
      const candlestickData = [];
      const response = await fetch("http://127.0.0.1:5001/api/market_summary", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ candlestick_data: candlestickData }),
      });
      const data = await response.json();
      if (data.summary) {
        setSummary(data.summary);
      } else {
        setSummary("Error fetching summary.");
      }
    } catch (error) {
      console.error("Error fetching summary:", error);
      setSummary("Error fetching summary.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-3">
      <h3 className="font-semibold text-gray-900 dark:text-white">AI Market Summary</h3>
      <div className="mt-3">
        <button
          onClick={fetchSummary}
          className="w-full py-2 bg-primary text-white font-semibold rounded"
          disabled={isLoading}
        >
          {isLoading ? "Generating..." : "Generate Summary"}
        </button>
      </div>
      {summary && (
        <div className="mt-4 p-3 bg-gray-100 dark:bg-gray-900/50 rounded-lg">
          <p className="text-sm text-gray-900 dark:text-white">{summary}</p>
        </div>
      )}
    </div>
  );
};

export default AiSummaryPanel;
