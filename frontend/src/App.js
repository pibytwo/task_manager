import React, { useEffect, useState, useCallback } from "react";
import {
  Typography,
  Button,
  TextField,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  CircularProgress,
  Pagination,
  Box,
  Paper,
  IconButton,
  Chip,
  Zoom,
  DialogContentText,
  Snackbar,
  Slide,
  Grow,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import RefreshIcon from "@mui/icons-material/Refresh";
import axios from "axios";
import "./App.css";

const BASE_URL =
  window.env?.REACT_APP_BASE_URL || "http://localhost:8000/api/v1";

export default function TaskManagerApp() {
  const [tasks, setTasks] = useState([]);
  const [totalTasks, setTotalTasks] = useState(0);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [confirmDelete, setConfirmDelete] = useState({
    open: false,
    taskId: null,
  });
  const [toast, setToast] = useState({ open: false, message: "" });

  const pageSize = 10;

  const showToast = (message) => {
    setToast({ open: true, message });
    setTimeout(() => setToast({ open: false, message: "" }), 3000);
  };

  const fetchTasks = useCallback(
    async (pageNo = 1) => {
      setLoading(true);
      try {
        const res = await axios.get(
          `${BASE_URL}/tasks?page_no=${pageNo}&page_size=${pageSize}`
        );
        setTasks(res.data.records);
        setTotalTasks(res.data.total);
      } catch (err) {
        console.error("Failed to fetch tasks", err);
        showToast("Failed to fetch tasks");
        setTasks([]);
        setTotalTasks(0);
      } finally {
        setLoading(false);
      }
    },
    [pageSize]
  );

  useEffect(() => {
    fetchTasks(page);
  }, [page, fetchTasks]);

  const handleCreate = async () => {
    if (!title.trim() || !description.trim()) {
      showToast("Title and description are required");
      return;
    }
    try {
      await axios.post(`${BASE_URL}/tasks`, { title, description });
      setOpen(false);
      setTitle("");
      setDescription("");
      fetchTasks(page);
      showToast("Task created successfully");
    } catch (err) {
      console.error("Failed to create task", err);
      showToast("Failed to create task");
    }
  };

  const handleStatusChange = async (id, status) => {
    try {
      await axios.put(`${BASE_URL}/tasks/${id}`, { status });
      fetchTasks(page);
      showToast(`Task marked as ${status}`);
    } catch (err) {
      console.error("Failed to update task status", err);
      showToast("Failed to update task status");
    }
  };

  const confirmDeleteTask = (id) => {
    setConfirmDelete({ open: true, taskId: id });
  };

  const handleDelete = async () => {
    try {
      await axios.delete(`${BASE_URL}/tasks/${confirmDelete.taskId}`);
      setConfirmDelete({ open: false, taskId: null });
      fetchTasks(page);
      showToast("Task deleted successfully");
    } catch (err) {
      console.error("Failed to delete task", err);
      showToast("Failed to delete task");
    }
  };

  const formatToLocal = (utcString) => {
    const utcDate = new Date(utcString + "Z");
    return utcDate.toLocaleString();
  };

  const getStatusChip = (task) => {
    const isCompleted = task.status === "completed";
    const newStatus = isCompleted ? "pending" : "completed";
    return (
      <Zoom in>
        <Chip
          label={task.status.charAt(0).toUpperCase() + task.status.slice(1)}
          color={isCompleted ? "success" : "warning"}
          size="small"
          onClick={() => handleStatusChange(task.id, newStatus)}
          className="status-chip"
        />
      </Zoom>
    );
  };

  return (
    <Box className="main-container">
      <Paper elevation={3} className="paper-container">
        <Box className="header-bar">
          <Typography variant="h4" fontWeight={600}>
            Task Manager
          </Typography>
          <Box>
            <Button
              variant="outlined"
              onClick={() => fetchTasks(page)}
              startIcon={<RefreshIcon />}
              sx={{ mr: 1 }}
            >
              Refresh
            </Button>
            <Button variant="contained" onClick={() => setOpen(true)}>
              Add Task
            </Button>
          </Box>
        </Box>

        {loading ? (
          <Box className="spinner-box">
            <CircularProgress />
            <Typography variant="body2" mt={2}>
              Loading tasks…
            </Typography>
          </Box>
        ) : tasks.length === 0 ? (
          <Box className="empty-box">
            <Typography variant="body1" color="text.secondary">
              No tasks available
            </Typography>
          </Box>
        ) : (
          <>
          <Box className="table-scroll-wrapper">
            <Table size="small">
              <TableHead>
                <TableRow className="table-head">
                  <TableCell>
                    <strong>Title</strong>
                  </TableCell>
                  <TableCell>
                    <strong>Description</strong>
                  </TableCell>
                  <TableCell>
                    <strong>Status</strong>
                  </TableCell>
                  <TableCell>
                    <strong>Created At</strong>
                  </TableCell>
                  <TableCell>
                    <strong>Actions</strong>
                  </TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {tasks.map((task) => (
                  <Grow in key={task.id} timeout={300}>
                    <TableRow hover className="task-row">
                      <TableCell>{task.title}</TableCell>
                      <TableCell>{task.description}</TableCell>
                      <TableCell>{getStatusChip(task)}</TableCell>
                      <TableCell>{formatToLocal(task.created_at)}</TableCell>
                      <TableCell>
                        <IconButton
                          color="error"
                          onClick={() => confirmDeleteTask(task.id)}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </TableCell>
                    </TableRow>
                  </Grow>
                ))}
              </TableBody>
            </Table>
            </Box>
            <Pagination
              count={Math.ceil(totalTasks / pageSize)}
              page={page}
              onChange={(_, value) => setPage(value)}
              className="pagination"
            />
          </>
        )}
      </Paper>

      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>Add New Task</DialogTitle>
        <DialogContent>
          <TextField
            label="Title"
            fullWidth
            margin="dense"
            required
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <TextField
            label="Description"
            fullWidth
            margin="dense"
            required
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpen(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleCreate}>
            Create
          </Button>
        </DialogActions>
      </Dialog>

      <Dialog
        open={confirmDelete.open}
        onClose={() => setConfirmDelete({ open: false, taskId: null })}
      >
        <DialogTitle>Confirm Deletion</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Are you sure you want to delete this task? This action cannot be
            undone.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button
            onClick={() => setConfirmDelete({ open: false, taskId: null })}
          >
            Cancel
          </Button>
          <Button color="error" onClick={handleDelete}>
            Delete
          </Button>
        </DialogActions>
      </Dialog>

      <Snackbar
        open={toast.open}
        message={toast.message}
        anchorOrigin={{ vertical: "top", horizontal: "center" }}
        TransitionComponent={Slide}
      />
    </Box>
  );
}
