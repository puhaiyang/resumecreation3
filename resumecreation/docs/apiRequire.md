# API Documentation

## 1. 用户注册与认证相关 API

这些 API 将处理用户的注册、登录、退出以及用户认证的相关操作。

### 1.1 用户注册

- **URL**: `/api/register/`
- **方法**: `POST`
- **描述**: 处理用户注册，接收用户名、密码等信息。
- **请求示例**:

    ```json
    {
        "username": "john_doe",
        "password": "Password123",
        "email": "john@example.com"
    }
    ```

- **响应示例**:

    ```json
    {
        "message": "User registered successfully."
    }
    ```

### 1.2 用户登录

- **URL**: `/api/login/`
- **方法**: `POST`
- **描述**: 用户登录，返回会话信息或 JWT token。
- **请求示例**:

    ```json
    {
        "username": "john_doe",
        "password": "Password123"
    }
    ```

- **响应示例**:

    ```json
    {
        "token": "JWT-TOKEN-123456"
    }
    ```

### 1.3 用户认证检查

- **URL**: `/api/check-auth/`
- **方法**: `GET`
- **描述**: 检查用户是否已登录。
- **请求示例**: (无请求体)
- **响应示例**:

    ```json
    {
        "is_authenticated": true,
        "username": "john_doe"
        "is_admin": true
    }
    ```

### 1.4 用户登出

- **URL**: `/api/logout/`
- **方法**: `POST`
- **描述**: 注销当前登录的用户。
- **响应示例**:

    ```json
    {
        "message": "User logged out successfully."
    }
    ```

## 2. 简历管理相关 API

这些 API 用于处理用户创建、编辑和管理简历的相关操作。

### 2.1 创建简历

- **URL**: `/api/resumes/`
- **方法**: `POST`
- **描述**: 创建新的简历。
- **请求示例**:

    ```json
    {
        "title": "Software Engineer Resume",
        "content": "This is the content of the resume...",
        "template_id": 1
    }
    ```

- **响应示例**:

    ```json
    {
        "message": "Resume created successfully.",
        "resume_id": 123
    }
    ```

### 2.2 查看用户所有简历

- **URL**: `/api/resumes/`
- **方法**: `GET`
- **描述**: 获取当前用户的所有简历。
- **响应示例**:

    ```json
    [
        {
            "resume_id": 123,
            "title": "Software Engineer Resume",
            "created_at": "2024-01-01T10:00:00Z"
        },
        {
            "resume_id": 124,
            "title": "Data Scientist Resume",
            "created_at": "2024-02-15T14:00:00Z"
        }
    ]
    ```

### 2.3 获取简历详情

- **URL**: `/api/resumes/{resume_id}/`
- **方法**: `GET`
- **描述**: 获取特定简历的详细信息。
- **响应示例**:

    ```json
    {
        "resume_id": 123,
        "title": "Software Engineer Resume",
        "content": "This is the content of the resume...",
        "template_id": 1,
        "created_at": "2024-01-01T10:00:00Z"
    }
    ```

### 2.4 更新简历

- **URL**: `/api/resumes/{resume_id}/`
- **方法**: `PUT`
- **描述**: 更新已有简历的内容。
- **请求示例**:

    ```json
    {
        "title": "Updated Resume Title",
        "content": "Updated content of the resume...",
        "template_id": 2
    }
    ```

- **响应示例**:

    ```json
    {
        "message": "Resume updated successfully."
    }
    ```

### 2.5 删除简历

- **URL**: `/api/resumes/{resume_id}/`
- **方法**: `DELETE`
- **描述**: 删除指定的简历。
- **响应示例**:

    ```json
    {
        "message": "Resume deleted successfully."
    }
    ```

## 3. 简历模板管理相关 API

这些 API 用于处理简历模板的选择和管理。

### 3.1 获取所有简历模板

- **URL**: `/api/templates/`
- **方法**: `GET`
- **描述**: 获取所有可用的简历模板。
- **响应示例**:

    ```json
    [
        {
            "template_id": 1,
            "name": "Modern Template",
            "description": "A modern and clean resume template."
        },
        {
            "template_id": 2,
            "name": "Classic Template",
            "description": "A classic resume template."
        }
    ]
    ```

### 3.2 获取模板详情

- **URL**: `/api/templates/{template_id}/`
- **方法**: `GET`
- **描述**: 获取某个特定模板的详细信息。
- **响应示例**:

    ```json
    {
        "template_id": 1,
        "name": "Modern Template",
        "description": "A modern and clean resume template.",
        "fields": [
            "Name",
            "Email",
            "Phone",
            "Work Experience"
        ]
    }
    ```

## 4. 管理员相关 API

提供给管理员进行操作的接口，例如管理用户或简历。

### 4.1 获取所有用户

- **URL**: `/api/admin/users/`
- **方法**: `GET`
- **描述**: 获取所有注册用户的列表（管理员权限）。
- **响应示例**:

    ```json
    [
        {
            "user_id": 1,
            "username": "john_doe",
            "email": "john@example.com",
            "is_active": true
        },
        {
            "user_id": 2,
            "username": "jane_doe",
            "email": "jane@example.com",
            "is_active": true
        }
    ]
    ```

### 4.2 删除用户

- **URL**: `/api/admin/users/{user_id}/`
- **方法**: `DELETE`
- **描述**: 删除指定用户（管理员权限）。
- **响应示例**:

    ```json
    {
        "message": "User deleted successfully."
    }
    ```

## 5 获取头像 外部api

- **URL**: `https://ui-avatars.com/api/?name={name}&size={size}&background={bg}&color={color}`
- **方法**: `GET `
- **描述**: 获取头像

        name：生成头像的名称（如用户名）。
	    size：图片大小（默认 64px）。
	    background：背景颜色（16 进制 RGB 代码）。
	    color：字体颜色（16 进制 RGB 代码）。
- **响应示例**:
  
  ·GET https://ui-avatars.com/api/?name=John+Doe&size=128&background=0D8ABC&color=fff·