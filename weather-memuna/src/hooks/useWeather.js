import { useState, useEffect } from "react";

export default function useWeather({ location }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!location) return;

    const controller = new AbortController();
    setLoading(true);
    setError(null);

    const q = encodeURIComponent(location.trim());
    fetch(`/api/weather?q=${q}`, { signal: controller.signal })
      .then(async (res) => {
        let body = null;
        try {
          body = await res.json();
        } catch {
          body = null;
        }
        if (!res.ok) {
          throw new Error(body?.error || "City not found");
        }
        return body;
      })
      .then((res) => {
        setData(res);
        setLoading(false);
      })
      .catch((err) => {
        if (err.name === "AbortError") return;
        setError(err.message || "Something went wrong");
        setLoading(false);
        setData(null);
      });

    return () => controller.abort();
  }, [location]);

  return { data, loading, error };
}
