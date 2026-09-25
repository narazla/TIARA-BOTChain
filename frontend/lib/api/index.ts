import { apiClient } from "./client";
import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  User,
} from "@/lib/types";

export const authApi = {
  register: async (data: RegisterRequest): Promise<User> => {
    const response = await apiClient.post<User>("/auth/register", data);
    return response.data;
  },

  login: async (data: LoginRequest): Promise<LoginResponse> => {
    const response = await apiClient.post<LoginResponse>("/auth/login", data);
    return response.data;
  },

  me: async (): Promise<User> => {
    const response = await apiClient.get<User>("/auth/me");
    return response.data;
  },

  logout: async (): Promise<void> => {
    await apiClient.post("/auth/logout");
  },
};

export const elderlyApi = {
  getHome: async () => {
    const response = await apiClient.get("/elderly/home");
    return response.data;
  },
};

export const checkinApi = {
  start: async () => {
    const response = await apiClient.post("/checkins/start", {});
    return response.data;
  },

  submitAnswer: async (
    sessionId: string,
    data: {
      question_id: string;
      answer_text: string;
      response_delay_seconds?: number;
      recording_started_at?: string;
      recording_ended_at?: string;
    }
  ) => {
    const response = await apiClient.post(`/checkins/${sessionId}/answer`, data);
    return response.data;
  },

  uploadMedia: async (sessionId: string, formData: FormData) => {
    const response = await apiClient.post(
      `/checkins/${sessionId}/upload-media`,
      formData,
      { headers: { "Content-Type": "multipart/form-data" } }
    );
    return response.data;
  },

  finish: async (sessionId: string, totalDurationSeconds: number) => {
    const response = await apiClient.post(`/checkins/${sessionId}/finish`, {
      total_duration_seconds: totalDurationSeconds,
    });
    return response.data;
  },

  getHistory: async () => {
    const response = await apiClient.get("/checkins/history");
    return response.data;
  },
};

export const caregiverApi = {
  verifyPin: async (pin: string) => {
    const response = await apiClient.post("/caregiver/verify-pin", { pin });
    return response.data;
  },

  getDashboard: async () => {
    const response = await apiClient.get("/caregiver/dashboard");
    return response.data;
  },

  getAlerts: async () => {
    const response = await apiClient.get("/caregiver/alerts");
    return response.data;
  },

  getRecommendations: async () => {
    const response = await apiClient.get("/caregiver/recommendations");
    return response.data;
  },

  getReports: async () => {
    const response = await apiClient.get("/caregiver/reports");
    return response.data;
  },
};

export const guidanceApi = {
  ask: async (message: string, sessionContextId?: string) => {
    const response = await apiClient.post("/guidance/ask", {
      message,
      session_context_id: sessionContextId || null,
    });
    return response.data;
  },

  getHistory: async () => {
    const response = await apiClient.get("/guidance/history");
    return response.data;
  },
};

export const healthcareApi = {
  getDashboard: async () => {
    const response = await apiClient.get("/healthcare/dashboard");
    return response.data;
  },

  getPatients: async (riskLevel?: string) => {
    const params = riskLevel ? { risk_level: riskLevel } : {};
    const response = await apiClient.get("/healthcare/patients", { params });
    return response.data;
  },

  getPatient: async (patientId: string) => {
    const response = await apiClient.get(`/healthcare/patients/${patientId}`);
    return response.data;
  },
};
