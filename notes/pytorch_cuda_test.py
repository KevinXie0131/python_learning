import torch

touch_cuda = torch.cuda.is_available()
print(touch_cuda)
print(torch.cuda.get_device_name())
print(torch.cuda.get_device_capability())
print(torch.cuda.get_device_properties())

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"CUDA is available. Using device: {torch.cuda.get_device_name(0)}")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU.")

# Create a tensor on the CPU
while True:
    x_cpu = torch.randn(3, 3)
    print(f"\nTensor on CPU:\n{x_cpu}")

    # Move the tensor to the GPU if CUDA is available
    x_gpu = x_cpu.to(device)
    print(f"\nTensor on {device}:\n{x_gpu}")

    # Perform an operation on the GPU
    y_gpu = x_gpu * 2 + 1
    print(f"\nResult of operation on {device}:\n{y_gpu}")

    # Move the result back to the CPU (if it was on GPU)
    y_cpu = y_gpu.to("cpu")
    print(f"\nResult moved back to CPU:\n{y_cpu}")

    # Example of creating a tensor directly on the GPU
    if torch.cuda.is_available():
        z_gpu = torch.ones(2, 2, device=device)
        print(f"\nTensor created directly on GPU:\n{z_gpu}")